#!/usr/bin/env python
# coding=utf-8

'''

test api
'''
import requests
from pprint import pprint
from requests.sessions import Session
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class Test_Api(object):

    def __init__(self):
        self.base_url = 'http://127.0.0.1:5000/api/users/'
        self.session = Session()

    def test_create_user(self):
        uid = '0004'
        url = urljoin(self.base_url, uid)
        data = {
            'name': 'user0003',
            'password': '12345'
        }
        # response = self.session.post(url, data).json()
        response = requests.post(url, data)
        resp_json = response.json()
        # while resp_json['msg'] == u'user already existed.':
        #     for i in range(5):
        #         uid = u'000{0}'.format(i)
        #         url = urljoin(self.base_url, uid)
        #         print uid
        #         print url
        #         if i == 5:
        #             break

            # response = requests.post(url, data)
        print response.json()
        print response.content
        print response.cookies
        print response.headers
        print response.status_code
        print response.text
        # print self.session.headers
        # print self.session.cookies
        # print self.session.params

        pprint(response)

    def get_user(self):
        url = urljoin(self.base_url, '002')
        response = requests.get(url)
        # print response    
        print response.text
        print response.json()
        print response.content

    def update_user(self):
        url = urljoin(self.base_url, '001')
        resp = requests.put(url)
        print resp.json()

    def get_users(self):
        url = 'http://127.0.0.1:5000/api/users'
        response = requests.get(url)
        print response.content

if __name__ == '__main__':
    test = Test_Api()
    # test.test_create_user()
    test.get_user()
    test.update_user()
    test.get_users()