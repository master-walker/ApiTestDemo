#!/usr/bin/env python
#coding=utf-8

'''

test

'''

import requests
import unittest
import multiprocessing
import time
from api import api_server


class ApiServerUnittest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.api_server_process = multiprocessing.Process(
            target = api_server.app.run()
        )
        cls.api_server_process.start()
        time.sleep(0.1)

    #     cls.login_url = 'http://127.0.0.1:5000/login'
    #     cls.info_url = 'http://127.0.0.1:5000/info'
    #     cls.username = 'admin'
    #     cls.password = '123456'
    #
    # def test_login(self):
    #     """
    #     测试登录
    #     """
    #     data = {
    #         'username': self.username,
    #         'password': self.password
    #     }
    #     response = requests.post(self.login_url, data=data).json()
    #     print response
    #     assert response['status_code'] == 200
    #     assert response['msg'] == 'success'


    def tearDown(cls):
        cls.api_server_process.terminate()
