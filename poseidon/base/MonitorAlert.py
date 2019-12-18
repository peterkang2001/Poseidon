# coding=utf-8

"""
@author:songmengyun
@file: MonitorAlert.py
@time: 2019/06/27

"""
import json


# region 巡检method

class MonitorAlert():

    def __init__(self):
        pass

    def _get_xunjian_html_report_path(self, html_path, monitor=False):
        '''巡检html report路径：docker和本地'''
        if monitor == True:
            path = html_path.split('logs')
            return ''.join(['http://192.168.38.139:81', '/arch-qa', path[1]])
        else:
            path = html_path.split('/')[-4:] # 取后4位数
            path_last = '/'.join(path)
            return ''.join(['http://0.0.0.0:8000', '/',path_last])  # 希望本地启动一个htmp服务：python3.7 -m http.server

    def _read_json_file(self,file_path):
        '''读取json文件'''
        with open(file_path, 'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict

    def send_wx_warning(self, url, json_report_dict, monitor=False, metric=None):
        if monitor == True:
            summary = json_report_dict['report']['summary']
            if summary.get('failed'):
                msg = "\n总用例数:{0}\n成功:{1}\n<div class=\"highlight\">失败:{2}</div>跳过:{3}\n执行时长:{4}".format(
                    summary.get('num_tests'),
                    summary.get('passed', 0),
                    summary.get('failed', 0),
                    summary.get('skipped', 0),
                    summary.get('duration', 0)
                )
                # msg = '运行结果如下\n <div class=\"normal\">执行case:%s</div> <div class=\"green\">成功:%s</div> <div class=\"highlight\">失败:%s</div> <div class=\"gray\">跳过:%s</div>'%(summary.get('num_tests',0),summary.get('passed', 0),summary.get('failed', 0),summary.get('skipped', 0)),
                if metric:
                    metric = ''.join([metric, '.alert'])
                else:metric = 'qa'

                # 支持tags，条件分发
                # owl_data = {
                #     "metric": metric,  # 用来标记产线项目组，后面作为统计发送的频率
                #     "url": url,  # 用来在微信中，作为点击信息的回调地址
                #     "message": msg,  # 显示的信息主体，支持简单的css
                #     "tags": {
                #         "serviceName": " crontab-service3 ",
                #     }
                # }

                owl_data = {
                    "metric": metric,  # 用来标记产线项目组，后面作为统计发送的频率
                    "message": msg,  # 显示的信息主体，支持简单的css
                    "url": url,  # 用来在微信中，作为点击信息的回调地址

                }

                import requests
                print('发送请求体：{0}'.format(owl_data))
                re = requests.post("http://owl-alertrouter.intra.yeshj.com/alert/add", json=owl_data)
                print(re.content)

# endregion