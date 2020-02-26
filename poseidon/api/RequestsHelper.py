#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Author:       kangliang
   date:         2019-05-08
"""

import logging
import json
import requests
import time
import poseidon.base.CommonBase as cb
from poseidon.api.Curl_conf import Curl_conf
from pytest_testconfig import config as pyconfig
from io import BytesIO
from requests_toolbelt import MultipartEncoder
from datetime import datetime




class Requests:
    """
    使用该类可以直接发起http请求
    如果需要对url或者其他http请求辅助方法可以使用RequestUtils类中的方法
    """
    _http_mode = None
    _http_debug = None
    _default_header = None
    _retry_num = 3
    _timeout = 30

    def sendRequest(self, method, url, data=None, headers=None, cookie=None, files=None,
                    httpStatusExp=None, statusExp=None, needJson=True, bText=True,agent=None,
                    multipartEncodedContent=None,  **kwargs):
        # 根据_http_mode 来选择不同的http请求插件

        _method = method.strip().upper()

        if self.is_pycurl_model():
            logging.info("使用pycurl发送请求")
            resp = self._sendRequest_pycurl(_method , url, data, headers, cookie, files,
                    httpStatusExp, statusExp, needJson, bText,agent, **kwargs)
        else:
            logging.info("使用requests发送请求")
            if multipartEncodedContent:   # 使用multipart类型的请求
                resp = self._sendRequest_multipart(_method, url, headers, cookie, httpStatusExp, statusExp,
                                                   needJson, bText, multipartEncodedContent)
            else:
                resp = self._sendRequest_requests(_method , url, data, headers, cookie, files,
                                              httpStatusExp, statusExp, needJson, bText,agent, **kwargs)
        return resp

    def _sendRequest_pycurl(self, method, url, data=None, headers=None, cookie=None, files=None,
                            httpStatusExp=None, statusExp=None, needJson=True, bText=True, agent=None, **kwargs):
        '''
        pycurl发送发送API请求，支持application/x-www-form-urlencoded，application/json格式
        同时输出请求时间片段

        '''

        try:
            import pycurl

            b = BytesIO()  # 创建缓存对象
            c = pycurl.Curl()  # 创建一个curl对象
            c.setopt(pycurl.URL, url)
            c.setopt(pycurl.WRITEDATA, b)  # 设置资源数据写入到缓存对象
            if pyconfig["sections"].get('http').get("debug").lower() == 'true':
                c.setopt(pycurl.VERBOSE, True)

            logging.info("请求url: {}".format(url))
            logging.info("请求method: {}".format(method))

            if headers is None:
                c.setopt(pycurl.HTTPHEADER, self._default_header)
                logging.info("请求header: {}".format(self._default_header))
                logging.info("请求header type is: {}".format(type(self._default_header)))
            else:
                if isinstance(headers, list):
                    c.setopt(pycurl.HTTPHEADER, headers)
                    logging.info("请求header: {}".format(headers))
                    logging.info("请求header type is: {}".format(type(headers)))
                else:
                    c.setopt(pycurl.HTTPHEADER, self.conver_header_dict_2_list(headers))
                    logging.info("请求header: {}".format(self.conver_header_dict_2_list(headers)))
                    logging.info("请求header type is: {}".format(type(self.conver_header_dict_2_list(headers))))

            if agent:
                c.setopt(pycurl.USERAGENT, agent)  # agent加入c对象
                logging.info("请求agent:{}".format(agent))
            else:
                agent = self.get_agent()
                c.setopt(pycurl.USERAGENT, agent)  # agent加入c对象

            if cookie:
                c.setopt(pycurl.COOKIE, cookie)   # cookie加入c对象

            if data:
                new_headers = self.dict_key_to_lower(headers)
                if 'content-type' in new_headers and new_headers.get(
                    'content-type') == 'application/x-www-form-urlencoded':
                    c.setopt(pycurl.POSTFIELDS, self.conver_data_dict_to_str(data))
                    logging.info("请求data: {}".format(data))
                elif 'content-type' in new_headers and new_headers.get('content-type') == 'application/json':
                    c.setopt(pycurl.POSTFIELDS, json.dumps(data))
                    logging.info("请求data: {}".format(json.dumps(data)))

            if method == "GET":
                pass
            elif method == "PUT":
                c.setopt(pycurl.CUSTOMREQUEST, "PUT")
            elif method == "DELETE":
                c.setopt(pycurl.CUSTOMREQUEST, "DELETE")
            elif method == "POST":
                c.setopt(pycurl.CUSTOMREQUEST, "POST")
            elif method == "PATCH":
                c.setopt(pycurl.CUSTOMREQUEST, "PATCH")
            else:
                logging.error('not support method: {}'.format(method))

            # 增加容错处理，默认retry_num=3
            for i in range(self._retry_num):
                try:
                    self.bContinue = False
                    c.perform()

                    total_time = c.getinfo(pycurl.TOTAL_TIME)  # 上一请求总的时间
                    dns_time = c.getinfo(pycurl.NAMELOOKUP_TIME)  # 域名解析时间
                    connect_time = c.getinfo(pycurl.CONNECT_TIME)  # 远程服务器连接时间
                    redirect_time = c.getinfo(pycurl.REDIRECT_TIME)  # 重定向所消耗的时间
                    ssl_time = c.getinfo(pycurl.APPCONNECT_TIME)  # SSL建立握手时间
                    pretrans_time = c.getinfo(pycurl.PRETRANSFER_TIME)  # 连接上后到开始传输时的时间
                    starttrans_time = c.getinfo(pycurl.STARTTRANSFER_TIME)  # 接收到第一个字节的时间

                    transfer_time = total_time - starttrans_time  # 传输时间
                    serverreq_time = starttrans_time - pretrans_time  # 服务器响应时间，包括网络传输时间
                    if ssl_time == 0:
                        if redirect_time == 0:
                            clientper_time = pretrans_time - connect_time  # 客户端准备发送数据时间
                            redirect_time = 0
                        else:
                            clientper_time = pretrans_time - redirect_time
                            redirect_time = redirect_time - connect_time
                        ssl_time = 0
                    else:
                        clientper_time = pretrans_time - ssl_time

                        if redirect_time == 0:
                            ssl_time = ssl_time - connect_time
                            redirect_time = 0
                        else:
                            ssl_time = ssl_time - redirect_time
                            redirect_time = redirect_time - connect_time

                    connect_time = connect_time - dns_time
                    logging.info('请求总时间: %.3f ms' % (total_time * 1000))
                    logging.info('DNS域名解析时间 : %.3f ms' % (dns_time * 1000))
                    logging.info('TCP连接消耗时间 : %.3f ms' % (connect_time * 1000))
                    logging.info('重定向时间: %.3f ms' % (redirect_time * 1000))
                    logging.info('SSL握手消耗时间 : %.3f ms' % (ssl_time * 1000))
                    logging.info('客户端发送请求准备时间: %.3f ms' % (clientper_time * 1000))
                    logging.info('服务器处理时间: %.3f ms' % (serverreq_time * 1000))
                    logging.info('数据传输时间: %.3f ms' % (transfer_time * 1000))

                    reps_code = c.getinfo(pycurl.RESPONSE_CODE)   # 返回code
                    body = b.getvalue()
                    c.close()
                    break
                except Exception as e:
                    msg = "send request [%s] %s failed: %s" % (method, url, str(e))
                    logging.info(e)
                    logging.info(msg)
                    if (str(e).find('Max retries exceeded') > 0 or str(e).find('Read timed out') > 0 or str(e).find(
                        'Connection aborted') > -1) and i + 1 < self._retry_num:
                        time.sleep(10)
                        self.bContinueb = True
                        continue
                    assert False, msg
                finally:
                    if not self.bContinue:
                        pass

        except Exception as e:
            logging.error(e)

        if httpStatusExp:
            logging.info("校验httpStatusExp")
            cb.checkEqual(reps_code, httpStatusExp)

        resp = body.decode('utf-8')
        logging.info("响应response:{}".format(resp))

        if needJson:
            return json.loads(resp)
        else:
            return resp

    def _sendRequest_requests(self, method, url, data=None, headers=None, cookie=None, files=None,
                              httpStatusExp=None, statusExp=None, needJson=True, bText=True, agent=None, **kwargs):

        '''
        request发送发送API请求，支持application/x-www-form-urlencoded，application/json格式

        '''

        if headers is None:  # 如果header为空，默认header
            headers = self._default_header

        if isinstance(headers, list):
            headers = self.conver_header_list_2_dict(headers)

        new_headers = self.dict_key_to_lower(headers)
        if 'content-type' in new_headers and new_headers['content-type'] == 'application/x-www-form-urlencoded':
            data = data if data else None
        elif 'content-type' in new_headers and new_headers['content-type'] == 'application/json':
            data = json.dumps(data) if data else None
        if 'content_tyep' in new_headers and new_headers['content-type'] == 'multipart/form-data':
            files = files if files else None
            # files = {'file':open('xxx.xls', 'rb')}

        logging.info("请求url: {}".format(url))
        logging.info("请求method: {}".format(method))
        logging.info("请求header: {}".format(headers))
        logging.info("请求header type is: {}".format(type(headers)))
        logging.info("请求data: {}".format(data))

        # 增加容错处理，默认retry_num=3
        for i in range(self._retry_num):
            try:
                self.bContinue = False

                if method == "GET":
                    if "https" in url:
                        resp = requests.get(url, params=data, headers=headers, cookies=cookie, timeout=self._timeout,
                                            stream=True, verify=False)
                    else:
                        resp = requests.get(url, params=data, headers=headers, cookies=cookie, timeout=self._timeout,
                                            stream=True)
                elif method == "PUT":
                    if "https" in url:
                        resp = requests.put(url, data=data, headers=headers, cookies=cookie, timeout=self._timeout,
                                            stream=True, verify=False)
                    else:
                        resp = requests.put(url, data=data, headers=headers, cookies=cookie, timeout=self._timeout,
                                            stream=True)
                elif method == "DELETE":
                    if "https" in url:
                        resp = requests.delete(url, data=data, headers=headers, cookies=cookie, timeout=self._timeout,
                                               stream=True, verify=False)
                    else:
                        resp = requests.delete(url, data=data, headers=headers, cookies=cookie, timeout=self._timeout,
                                               stream=True)
                elif method == "POST":
                    if "https" in url:
                        resp = requests.post(url, data=data, files=files, headers=headers, cookies=cookie,
                                             timeout=self._timeout, stream=True, verify=False)
                    else:
                        resp = requests.post(url, data=data, files=files, headers=headers, cookies=cookie,
                                             timeout=self._timeout, stream=True)
                elif method == "PATCH":
                    if "https" in url:
                        resp = requests.patch(url, data=data, headers=headers, cookies=cookie, timeout=self._timeout,
                                              stream=True, verify=False)
                    else:
                        resp = requests.patch(url, data=data, headers=headers, cookies=cookie, timeout=self._timeout,
                                              stream=True)
                else:
                    logging.error("The request method %s is not in ['post','get','put','delete','patch']")
                    assert False

                break

            except Exception as e:
                msg = "send request [%s] %s failed: %s" % (method, url, str(e))
                logging.info(e)
                logging.info(msg)
                if (str(e).find('Max retries exceeded') > 0 or str(e).find('Read timed out') > 0 or str(e).find(
                    'Connection aborted') > -1) and i + 1 < self._retry_num:
                    time.sleep(10)
                    self.bContinueb = True
                    continue
                assert False, msg
            finally:
                if not self.bContinue:
                    pass

        # 校验httpStatusCode
        if httpStatusExp:
            logging.info("校验httpStatusExp")
            cb.checkResultEqual(resp.status_code, httpStatusExp,
                                f'actual status_code: {resp.status_code}, expect status_code: {httpStatusExp}')

        # 输出响应头和响应内容
        logging.info('响应headers: {}'.format(resp.headers))

        if needJson:
            if bText:
                resp_text = resp.text
            else:
                resp_text = resp.content
            resp = cb.loadJsonData(resp_text)
            logging.info("响应response: {}".format(resp))
            if statusExp:
                cb.checkValueInDict(resp, "status", statusExp,
                                    "[Request] resp data['status'] does not match with %s" % str(statusExp))
        return resp

    def _sendRequest_multipart(self, method, url, headers=None, cookie=None, httpStatusExp=None, statusExp=None,
                               needJson=True, bText=True, multipartEncodedContent=None):
        '''
        Send Multipart request with method post or put
        '''
        if not isinstance(multipartEncodedContent, MultipartEncoder):
            raise RuntimeError("multipartEncodedContent invalid")

        if headers is None:  # 如果header为空，默认header
            headers = self._default_header

        if isinstance(headers, list):
            headers = self.conver_header_list_2_dict(headers)

        headers.update({'Content-Type': multipartEncodedContent.content_type})
        try:
            if method == "POST":
                if "https" in url:
                    resp = requests.post(url, data=multipartEncodedContent, headers=headers,
                                         verify=False, cookies=cookie)
                else:
                    resp = requests.post(url, data=multipartEncodedContent, headers=headers,
                                         cookies=cookie)
            elif method == "PUT":
                if "https" in url:
                    resp = requests.put(url, data=multipartEncodedContent, headers=headers,
                                        verify=False, cookies=cookie)
                else:
                    resp = requests.put(url, data=multipartEncodedContent, headers=headers,
                                        cookies=cookie)
        except Exception as e:
            print("[Request Exception] {0}: {1}".format(type(e), e))
            msg = "send request {%s] %s failed: %s" % (method, url, str(e))
            logging.error(e)
            logging.error(msg)
            assert False, msg

        if httpStatusExp:
            logging.info("校验httpStatusExp")
            cb.checkResultEqual(resp.status_code, httpStatusExp,
                                f'actual status_code: {resp.status_code}, expect status_code: {httpStatusExp}')

        # 输出响应头信息
        logging.info('响应headers: {}'.format(resp.headers))

        if needJson:
            if bText:
                resp_text = resp.text
            else:
                resp_text = resp.content
            resp = cb.loadJsonData(resp_text)
            if statusExp:
                cb.checkValueInDict(resp, "status", statusExp,
                                            "[Request] resp data['status'] does not match with %s" % str(statusExp))
        return resp



    #region function

    def get_default_header_pycurl(self, templateName='default_header_template_1_pycurl'):
        conf = Curl_conf()
        self._default_header = conf.__getattribute__(templateName)
        return self._default_header


    def get_agent(self,templateName = "useragent_firefox_pc"):
        conf = Curl_conf()
        return conf.__getattribute__(templateName)


    def is_pycurl_model(self):
        if pyconfig["sections"].get('http').get('mode').strip().lower() == 'pycurl':
            return True
        else:
            return False

    def conver_header_list_2_dict(self, headers):
        my_dict = {}
        try:
            for item in enumerate(headers):
                _group = item[1].split(":")
                my_dict[_group[0].strip()] = _group[1].strip()
        except Exception as e:
            logging.error(e)
        return my_dict

    def conver_header_dict_2_list(self, headers):
        my_list = []

        if isinstance(headers, dict):
            try:
                for key, value in headers.items():
                    _item = "{key}:{value}".format(key=key, value=value)
                    my_list.append(_item)
            except Exception as e:
                logging.error(e)

        return my_list

    def conver_data_dict_to_str(self, data):
        if data:
            from urllib import parse
            data_str = parse.urlencode(data)
            return data_str

    def dict_key_to_lower(self, dict):
        if dict:
            new_dict = {}
            for key, value in dict.items():
                new_dict[key.lower()] = value
            return new_dict


#endregion



