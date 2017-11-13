#!/usr/bin/env python
#coding=utf-8

import requests
import os

METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']

config_path = os.path.abspath(__file__)
    # os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]


class UnSupportMethodException(Exception):
    """当传入的method的参数不是支持的类型时抛出此异常。"""
    pass

url = "http://www.baidu.com"

class Httpclient(object):
    """
       http请求的client。初始化时传入url、method等，可以添加headers和cookies，但没有auth、proxy。

       >>> HTTPClient('http://www.baidu.com').send()
       <Response [200]>

       """

    def __init__(self, url, method="GET", headers=None, cookies=None):
        self.url = url
        self.session = requests.session()
        self.method = method.upper()
        if self.method not in METHODS:
            raise UnSupportMethodException("不支持")

        self.set_headers(headers)

    def set_headers(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookie(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self, params=None, data=None, **kwargs):
        response = self.session.request(method=self.method, url=self.url, params=params, data=data, **kwargs)
        response.encoding = 'utf-8'
        print u'{0} {1} '.format(self.method, self.url)
        print u'{0} \n {1}'.format(response, response.text)
        return response

if __name__ == "__main__":
    httpclient=Httpclient(url)
    httpclient.send()