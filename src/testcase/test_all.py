#!/usr/bin/env python
# coding=utf-8

'''
测试类

'''
import requests, json
from requests.sessions import Session
from pprint import pprint
from utils import common


ses=Session()

USER="sdjk125"
PASSWORD="hs001471"
with open('test.txt', 'r') as f:
    # while 1:
    # keys = f.readlines()
    # print keys
    # for n, k in enumerate(keys):
    #     print "{0}: {1}".format(n, k)
    i = 0
    for key in f:
        if not key:
            break
        key = key.strip()
        # keys = [key]
        i = i + 1
        # print keys
        # for k in enumerate(key):
        print "{0}: {1}".format(i,key)



def get_json_data():
    with open('../data/test.json', 'r') as f:
        data = json.load(f)
        return data
        # print data
data = get_json_data()
request_data = data['login_case']
print request_data['request']['url']

# print request_data['headers']
# print request_data.pop('url')
# print data['response']


def run_testcase():
    request_data = common.get_json_data()
    request_json = request_data['login_case']['request']
    url = request_json['url']
    method = request_json['method']
    data = request_json['json']
    expected_response = request_data['login_case']['response']
    resp_obj = requests.request(url=url,method=method,data=data)
    diff_json = common.diff_content(resp_obj,expected_response)
    success =False if diff_json else True
    return success,diff_json

result, diff = run_testcase()
print result
print diff



def test_get():

    url="https://www.baidu.com"


    response=requests.get(url)
    resp=ses.get(url)
    header=ses.headers

    print resp
    print header
    print response

def test_post():
    url="https://www.gcall.com"

    data={
        "username": USER,
        "password": PASSWORD
    }
    resp=requests.post(url,data=data)
    resp2=ses.post(url,data=data)
    header=ses.headers
    cks=requests.post(url,data=data).cookies
    session=cks.get("session")
    print session
    print resp
    print resp2
    print header


# test_post()

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
    #
    # def test_info(self):
    #     """
    #     测试info接口
    #     """
    #     data = {
    #         'username': self.username,
    #         'password': self.password
    #     }
    #     response_cookies = requests.post(self.login_url, data=data).cookies
    #     session = response_cookies.get('session')
    #     assert session
    #     info_cookies = {
    #         'session': session
    #     }
    #     response = requests.get(self.info_url, cookies=info_cookies).json()
    #     assert response['status_code'] == 200
    #     assert response['msg'] == 'success'
    #     assert response['data'] == 'info'

class DemoApi(object):
    def __init__(self, base_url):
        self.base_url = base_url
        # 创建session实例
        self.session = Session()

    def login(self, username, password):
        """
        登录接口
        :param username: 用户名
        :param password: 密码
        """
        url = urljoin(self.base_url, 'login')
        data = {
            'username': username,
            'password': password
        }
        response = self.session.post(url, data=data).json()
        print('\n*****************************************')
        print(u'\n1、请求url: \n%s' % url)
        print(u'\n2、请求头信息:')
        pprint(self.session.headers)
        print(u'\n3、请求参数:')
        pprint(data)
        print(u'\n4、响应:')
        pprint(response)
        return response

    def info(self):
        """
        详情接口
        """
        url = urljoin(self.base_url, 'info')
        response = self.session.get(url).json()
        print('\n*****************************************')
        print(u'\n1、请求url: \n%s' % url)
        print(u'\n2、请求头信息:')
        pprint(self.session.headers)
        print(u'\n3、请求cookies:')
        pprint(dict(self.session.cookies))
        print(u'\n4、响应:')
        pprint(response)
        return response


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_url = 'http://127.0.0.1:5000'
        cls.username = 'admin'
        cls.password = '123456'
        cls.app = DemoApi(cls.base_url)

    def test_login(self):
        """
        测试登录
        """
        response = self.app.login(self.username, self.password)
        assert response['code'] == 200
        assert response['msg'] == 'success'

    def test_info(self):
        """
        测试获取详情信息
        """
        self.app.login(self.username, self.password)
        response = self.app.info()
        assert response['code'] == 200
        assert response['msg'] == 'success'
        assert response['data'] == 'info'