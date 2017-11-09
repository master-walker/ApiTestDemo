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

