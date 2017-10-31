#!/usr/bin/python
# coding=utf-8
import os
import requests
import unittest
import subprocess
import functools
from utils.api_server_unittest import ApiServerUnittest

'''

'''


# def request(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         return func
#
#     return wrapper



class TestApiServer(unittest.TestCase):

    def setUp(self):
        # self.base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        # print self.base_path
        # api_path = os.path.join(self.base_path, '/api')
        # print api_path
        # subprocess.check_output('cd /Users/colin/MyDisk/myfiles/python/ApiTestDemo/src/api')
        # subprocess.check_output('python api_server.py')
        # super(TestApiServer, self).setUp()
        self.login_url = 'http://127.0.0.1:5000/login'
        self.info_url = 'http://127.0.0.1:5000/info'
        self.username = 'admin'
        self.password = '123456'



    def test_login(self):
        """
        测试登录
        """
        data = {
            'username': self.username,
            'password': self.password
        }
        response = requests.post(self.login_url, data=data).json()
        print response
        assert response['status_code'] == 200
        assert response['msg'] == 'success'

    def test_info(self):
        """
        测试info接口
        """
        data = {
            'username': self.username,
            'password': self.password
        }
        response_cookies = requests.post(self.login_url, data=data).cookies
        session = response_cookies.get('session')
        assert session
        info_cookies = {
            'session': session
        }
        response = requests.get(self.info_url, cookies=info_cookies).json()
        assert response['status_code'] == 200
        assert response['msg'] == 'success'
        assert response['data'] == 'info'

    def tearDown(self):
        pass
        # super(TestApiServer, self).tearDown()


if __name__ == '__main__':
    unittest.main()
