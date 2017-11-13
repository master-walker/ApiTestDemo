#!/usr/bin/python
# coding=utf-8
import os
import requests
from requests.sessions import Session
import unittest, traceback
import ast
import subprocess
import functools
from utils.api_server_unittest import ApiServerUnittest
from openpyxl import load_workbook
from utils import common
try:
    from urlparse import urljoin
except:
    from urllib.parse import urljoin
from testcase.test_api import test_create_user


class TestApiServer(unittest.TestCase):

    def setUp(self):
        self.session = Session()
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

    def test_all_api(self):
        test_create_user()

    def tearDown(self):
        pass
        # super(TestApiServer, self).tearDown()


if __name__ == '__main__':
    unittest.main()
