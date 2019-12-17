#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Author:       kangliang
   date:         2019-05-08
"""
from Tetis.api.Curl_conf import Curl_conf
from pytest_testconfig import config as pyconfig
from io import BytesIO
import logging, json
import time
import Tetis.base.CommonBase as cb

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
                    httpStatusExp=None, statusExp=None, needJson=True, bText=True,agent=None, **kwargs):
        # 根据_http_mode 来选择不同的http请求插件

        _method = method.strip().upper()

        if self.is_pycurl_model():
            logging.info("使用pycurl发送请求")
            resp = self._sendRequest_pycurl(_method , url, data, headers, cookie, files,
                    httpStatusExp, statusExp, needJson, bText,agent, **kwargs)
        else:
            logging.info("使用requests发送请求")
            resp = self._sendRequest_requests(_method , url, data, headers, cookie, files,
                                              httpStatusExp, statusExp, needJson, bText,agent, **kwargs)

        return resp

    def _sendRequest_pycurl(self, method, url, data=None, headers=None, cookie=None, files=None,
                    httpStatusExp=None, statusExp=None, needJson=True, bText=True,agent=None, **kwargs):
        try:
            import pycurl

            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(pycurl.URL,url)
            c.setopt(pycurl.WRITEDATA, buffer)
            if pyconfig["sections"].get('http').get("debug").lower() == 'true':
                c.setopt(pycurl.VERBOSE, True)


            if headers is None:
                c.setopt(pycurl.HTTPHEADER, self._default_header)
                logging.info("请求header:{}".format(self._default_header))
                logging.info("请求header type is :{}".format(type(self._default_header)))
            else:
                if isinstance(headers, list):
                    c.setopt(pycurl.HTTPHEADER, headers)
                    logging.info("请求header:{}".format(headers))
                    logging.info("请求header type is :{}".format(type(headers)))
                else:
                    _headers = self.conver_header_dict_2_list(headers)
                    c.setopt(pycurl.HTTPHEADER, _headers)
                    logging.info("请求header:{}".format(headers))
                    logging.info("请求header type is :{}".format(type(headers)))

            if agent is None:
                c.setopt(pycurl.USERAGENT, self.get_agent())
                logging.info("请求agent:{}".format(self.get_agent()))
            else:
                c.setopt(pycurl.USERAGENT, agent)
                logging.info("请求agent:{}".format(agent))

            if data is not None:
                new_headers = self.dict_key_to_lower(headers)
                if 'content-type' in new_headers and new_headers.get('content-type') == 'application/x-www-form-urlencoded':
                    c.setopt(pycurl.POSTFIELDS, self.conver_data_dict_to_str(data))
                    logging.info("请求data:{}".format(data))
                else:
                    c.setopt(pycurl.POSTFIELDS, json.dumps(data))
                    logging.info("请求data:{}".format(json.dumps(data)))
            else:
                logging.info("请求data:{}".format(None))

            if method == "GET":
                logging.info("请求method:{}".format(method))
                pass
            elif method == "PUT":
                logging.info("请求method:{}".format(method))
                c.setopt(pycurl.CUSTOMREQUEST, "PUT")
            elif method == "DELETE":
                logging.info("请求method:{}".format(method))
                c.setopt(pycurl.CUSTOMREQUEST, "DELETE")
            elif method == "POST":
                logging.info("请求method:{}".format(method))
                c.setopt(pycurl.CUSTOMREQUEST, "POST")
            elif method == "PATCH":
                logging.info("请求method:{}".format(method))
                c.setopt(pycurl.CUSTOMREQUEST, "PATCH")
            else:
                pass


            # 增加容错处理，默认retry_num=3
            for i in range(self._retry_num):
                try:
                    self.bContinue = False
                    c.perform()
                    c.close()
                    body = buffer.getvalue()
                    break
                except Exception as e:
                    msg = "send request [%s] %s failed: %s" % (method, url, str(e))
                    logging.info(e)
                    logging.info(msg)
                    if (str(e).find('Max retries exceeded') > 0 or str(e).find('Read timed out') > 0 or str(e).find('Connection aborted') > -1) and i + 1 < self._retry_num:
                        time.sleep(10)
                        self.bContinueb = True
                        continue
                    assert False, msg
                finally:
                    if not self.bContinue:
                        pass

            resp = body.decode('utf-8')
            if needJson:
                logging.info("响应response:{}".format(resp))
                return json.loads(resp)

            else:
                logging.info("响应response:{}".format(resp))
                return resp
        except Exception as e:
            logging.error("看看看")
            logging.error(e)


    def _sendRequest_requests(self, method, url, data=None, headers=None, cookie=None, files=None,
                    httpStatusExp=None, statusExp=None, needJson=True, bText=True,agent=None, **kwargs):

        import requests
        if isinstance(headers, list):
            headers = self.conver_header_list_2_dict(headers)

        # 如果发送请求为x-www-form-urlencoded，需把value转为str
        new_headers = self.dict_key_to_lower(headers)
        if 'content-type' in new_headers and new_headers.get('content-type') == 'application/x-www-form-urlencoded':
            data = self.conver_data_dict_to_str(data) if data else None
            logging.info("请求data:{}".format(data if data else data))
        else:
            data = json.dumps(data) if data else None
            logging.info("请求data:{}".format(json.loads(data) if data else data))

        logging.info("请求url:{}".format(url))
        logging.info("请求header:{}".format(json.dumps(headers)))
        logging.info("请求header type is :{}".format(type(headers)))
        logging.info("请求method:{}".format(method))

        # 增加容错处理，默认retry_num=3
        for i in range(self._retry_num):
            try:
                self.bContinue = False

                if method == "GET":
                    if "https" in url:
                        resp = requests.get(url, cookie, headers=headers, timeout=self._timeout, stream=True,
                                            verify=False)
                    else:
                        resp = requests.get(url,cookie, headers=headers, timeout=self._timeout, stream=True)

                elif method == "PUT":
                    if "https" in url:
                        resp = requests.put(url,data=data, headers=headers,  timeout=self._timeout, stream=True,
                                             verify=False)
                    else:
                        resp = requests.put(url, data=data, headers=headers, timeout=self._timeout, stream=True)

                elif method == "DELETE":
                    if "https" in url:
                        resp = requests.delete(url, data=data, headers=headers, timeout=self._timeout, stream=True,
                                             verify=False)
                    else:
                        resp = requests.delete(url, data=data,  headers=headers, timeout=self._timeout, stream=True)

                elif method == "POST":
                    if "https" in url:
                        resp = requests.post(url,data=data, headers=headers, timeout=self._timeout,stream=True,
                                             verify=False)
                    else:
                        resp = requests.post(url, data=data, headers=headers, timeout=self._timeout,stream=True)

                elif method == "PATCH":
                    if "https" in url:
                        resp = requests.patch(url, data=data, headers=headers, timeout=self._timeout,stream=True,
                                             verify=False)
                    else:
                        resp = requests.patch(url, data=data, headers=headers, timeout=self._timeout,stream=True)
                else:
                    logging.error("The request method %s is not in ['post','get','put','delete','patch']")
                    assert False

                break

            except Exception as e:
                msg = "send request [%s] %s failed: %s" % (method, url, str(e))
                logging.info(e)
                logging.info(msg)
                if (str(e).find('Max retries exceeded') > 0 or str(e).find('Read timed out') > 0 or str(e).find('Connection aborted') > -1) and i + 1 < self._retry_num:
                    time.sleep(10)
                    self.bContinueb = True
                    continue
                assert False, msg
            finally:
                if not self.bContinue:
                    pass

        # 校验httpStatusCode
        if httpStatusExp is not None:
            logging.info("校验status_code")
            cb.checkEqual(resp.status_code, int(httpStatusExp))

        resp = resp.text
        logging.info("响应response:{}".format(resp))
        if needJson:
            return json.loads(resp)
        else:
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



