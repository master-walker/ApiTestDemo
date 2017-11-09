#!/usr/bin/env python
# coding=utf-8

'''
test api
'''
import ast
import requests,traceback
from pprint import pprint
from requests.sessions import Session
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin
from openpyxl import load_workbook
from utils import common


ws = common.get_sheet('../data/TestCase.xlsx','TestCase')

row_data = common.get_row_data(ws,1)
# print row_data
url_path =  row_data[3]
data = row_data[6]
expected_resp = row_data[8]
print expected_resp
expected_resp = ast.literal_eval(expected_resp)
print type(expected_resp)


class Test_Api(object):

    def __init__(self):
        self.base_url = row_data[2]
            # 'http://127.0.0.1:5000/api/users/'
        self.session = Session()

    def test_create_user(self):
        url = urljoin(self.base_url, url_path)
        response = self.session.post(url, data)#.json()
        # response = requests.post(url, data)
        resp_json = response.json()

        print response
        print resp_json
        print type(resp_json)
        try:
            assert resp_json == dict(expected_resp) and response.status_code == 200
        except AssertionError:
            print traceback.print_exc()
            # response = requests.post(url, data)
        # print response.json()
        # print response.content
        # print response.cookies
        # print response.headers
        # print response.status_code
        # print response.text
        # print self.session.headers
        # print self.session.cookies
        # print self.session.params

    def get_user(self):
        url = urljoin(self.base_url, '002')
        response = self.session.get(url)
        # print response    
        print response.text
        print response.json()
        print response.content

    def update_user(self):
        url = urljoin(self.base_url, '001')
        resp = self.session.post(url)
        print resp.json()

    def get_users(self):
        url = 'http://127.0.0.1:5000/api/users'
        response = self.session.get(url)
        print response.content

if __name__ == '__main__':
    test = Test_Api()
    test.test_create_user()
    # test.get_user()
    # test.update_user()
    # test.get_users()