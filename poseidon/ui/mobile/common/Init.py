# coding=utf-8

"""
@author:songmengyun
@file: Init.py
@time: 2020/01/08

"""


import json
import logging
import subprocess
import sys
import os
import redis
import requests
import time

class Init(object):

    def _execute(self, method=None, url=None, data=None, json_data=None, timeout=30, serial=None):
        result = {}
        maxtime = time.time() + float(timeout)
        while time.time() < maxtime:
            if "GET" == method:
                try:
                    result = json.loads(requests.get(url, timeout=timeout).text)
                except Exception as e:
                    logging.debug("URL is %s, result is %s" % (url, e))
                    if str(e).find('timeout') > -1:
                        self.ip = self.get_ip(serial)
                    result = {"status": "error",
                              "value": "连接异常，请检查设备:'{0}'端服务是否成功启动,或者检查设备是否连上'hujiang'无线网".format(serial)}
                    time.sleep(1)
                    continue
            elif "POST" == method:
                try:
                    result = json.loads(requests.post(url, timeout=timeout, data=data, json=json_data).text)
                except Exception as e:
                    logging.debug("URL is %s, result is %s" % (url, e))
                    if str(e).find('timeout') > -1:
                        self.ip = self.get_ip(serial)
                    result = {"status": "error",
                              "value": "连接异常，请检查设备:'{0}'端服务是否成功启动,或者检查设备是否连上'hujiang'无线网".format(serial)}
                    time.sleep(1)
                    continue
            elif "DELETE" == method:
                try:
                    result = json.loads(requests.delete(url, timeout=timeout).text)
                except Exception as e:
                    logging.debug("URL is %s, result is %s" % (url, e))
                    if str(e).find('timeout') > -1:
                        self.ip = self.get_ip(serial)
                    result = {"status": "error",
                              "value": "连接异常，请检查设备:'{0}'端服务是否成功启动,或者检查设备是否连上'hujiang'无线网".format(serial)}
                    time.sleep(1)
                    continue

            if not result['value']:
                time.sleep(1)
                continue
            else:
                break

        log_msg = str(result)
        if len(log_msg) > 300:
            log_msg = log_msg[0:300]
        logging.info("URL is %s, result is %s" % (url, log_msg))
        return result

    @staticmethod
    def shell(cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)  # , close_fds=True)
        out, err = p.communicate()
        if p.returncode != 0:
            logging.warning('please make sure you have installed the target cmd on your computer to execute "{0}" OR 设备不被支持  !!!'.format(cmd))
            # sys.exit(0)
            return "error"
        return out.decode('utf-8')

    def get_devices(self):
        cmd = 'adb devices'
        try:
            data = self.shell(cmd)
            data = data.strip('List of devices attached').split()
            device_list = [x for x in data if x != 'device']
            if len(device_list) > 0:
                return device_list
            else:
                logging.info('No devices list, please start a deivce first!')
                return []
        except Exception as e:
            print(e)

    def start_appium_server(self):
        print()

    def start_android_server(self, serial):
        count = 5
        cmd = "adb -s {0} shell exec nohup app_process -Djava.class.path=/data/local/tmp/app-process.apk /system/bin com.yyl.android.Main >/dev/null 2>&1 &".format(serial)
        self.shell(cmd)
        time.sleep(5)
        ip = self.get_ip(serial)

        while self.status_android_server(ip, serial)['status'] == 'error' and count > 0:
            count = count - 1
            self.shell(cmd)

    @staticmethod
    def download(url, target_file_path):
        r = requests.get(url, stream=True)
        with open(target_file_path, "wb") as pdf:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)

    def start_uiautomator_ui(self, serial):
        logging.info("启动uiautomator ui")
        return self.shell(
            cmd="am start -a android.intent.action.VIEW -n com.yyl.android.hj.auto/com.yyl.android.hj.auto.MainActivity -W")

    def get_ip(self, serial):
        self.start_uiautomator_ui(serial)
        r = redis.Redis(host='192.168.160.188', port=6379, db=15)
        device_detail = r.get(serial)
        device_detail = json.loads(device_detail.decode('utf-8'))
        ip = device_detail['host']
        if not ip:
            print("检查设备{0}是否连上'hujiang'无线网")
            return ''
        else:
            return ip

    def start_hj_auto(self, serial):
        cmd = "adb -s {0} shell am start -a android.intent.action.VIEW -n com.yyl.android.hj.auto/com.yyl.android.hj.auto.MainActivity -W".format(
            serial)
        self.shell(cmd)

    def status_android_server(self, ip, serial):
        logging.info("通过ip检查设备:{0} 60002服务是否成功启动".format(serial))
        return self._execute(method="GET", url="http://{0}:{1}/health".format(ip, 60002), serial=serial)

    def reboot(self, num):
        devices = self.get_devices()
        for device in devices:
            init.shell("adb -s {0} shell reboot".format(device))
        while True:
            time.sleep(10)
            devices = init.get_devices()
            if len(devices) < num:
                continue
            else:
                time.sleep(15)
                break


if __name__ == '__main__':
    try:
        # if len(sys.argv) < 2:
        #     print("请指定初始化设备数")
        #     sys.exit(0)
        # print("初始化设备数为: {0} ".format(sys.argv[1]))
        init = Init()
        devices = init.get_devices()
        # if len(devices) < int(sys.argv[1]):
        #     print("请检查设备是否都能成功连接电脑，当前连接数为: {0},指定初始化设备数为:{1} ".format(len(devices), sys.argv[1]))
        #     sys.exit(0)
        path_apk = os.getcwd()
        print("apk下载目录 : " + os.getcwd())
        print("设备重启中,请稍等片刻...")

        init.reboot(int(sys.argv[1]))
        print("设备重启执行完成")

        print(os.path.abspath(path_apk + "/" + "app-process.apk"))

        init.download(url="http://192.168.160.188:8080/download2/app-process.apk",
                      target_file_path=os.path.abspath(path_apk + "/" + "app-process.apk"))
        print("'app-process.apk'下载执行完成")

        init.download(
            url="http://192.168.160.188:8080/download2/uiautomator2.androidTest.apk",
            target_file_path=os.path.abspath(path_apk + "/" + "uiautomator2.androidTest.apk"))
        print("'uiautomator2.androidTest.apk'下载执行完成")

        init.download(url="http://192.168.160.188:8080/download2/uiautomator2-server.apk",
                      target_file_path=os.path.abspath(path_apk + "/" + "uiautomator2-server.apk"))
        print("'uiautomator2-server.apk'下载执行完成")

        init.download(url="http://192.168.160.188:8080/download2/hj_auto.apk",
                      target_file_path=os.path.abspath(path_apk + "/" + "hj_auto.apk"))
        print("'hj_auto.apk'下载执行完成")

        for device in devices:
            init.shell("adb -s {0} shell pm uninstall io.appium.uiautomator2.server && adb -s {1} shell pm uninstall io.appium.uiautomator2.server.test && adb -s {2} shell pm uninstall com.yyl.android.hj.auto").format(device,device,device)
            print(init.shell("adb -s {0} shell input swipe 300 1500 300 0 100".format(device)))
            print(init.shell("adb -s {0} shell input keyevent 3".format(device)))
            print("准备执行安装'uiautomator2.androidTest.apk'")
            init.shell("adb -s {0} push {1} /sdcard/Download/".format(device, os.path.abspath(path_apk + "/" + "uiautomator2.androidTest.apk")))
            print(init.shell("adb -s {0} install -r {1}".format(device, os.path.abspath(path_apk + "/" + "uiautomator2.androidTest.apk"))))

            print("准备执行安装'uiautomator2-server.apk.apk'")
            init.shell("adb -s {0} push {1} /sdcard/Download/".format(device, os.path.abspath(path_apk + "/" + "uiautomator2-server.apk")))
            print(init.shell("adb -s {0} install -r {1}".format(device, os.path.abspath(path_apk + "/" + "uiautomator2-server.apk"))))

            print("准备执行安装'hj_auto.apk'")
            init.shell("adb -s {0} push {1} /sdcard/Download/".format(device, os.path.abspath(path_apk + "/" + "hj_auto.apk")))
            print(init.shell("adb -s {0} install -r {1}".format(device, os.path.abspath(path_apk + "/" + "hj_auto.apk"))))

            print("准备执行安装'app-process.apk'")
            init.shell("adb -s {0} push {1} /data/local/tmp/".format(device, os.path.abspath(path_apk + "/" + "app-process.apk")))

            print("准备启动'60002服务'")
            init.start_android_server(device)

            print("准备打开'hj_auto'")
            init.start_hj_auto(device)

    except Exception as e:
        print(e)
