#!/usr/bin/env python
# coding=utf-8

'''
utils function
'''
from openpyxl import load_workbook
import json
from pprint import pprint


def print_log(session, url, data):
    response = session.post(url, data=data).json()
    print('\n*****************************************')
    print(u'\n1、请求url: \n%s' % url)
    print(u'\n2、请求头信息:')
    pprint(session.headers)
    print(u'\n3、请求参数:')
    pprint(data)
    print(u'\n4、响应:')
    pprint(response)

def get_json_data():
    with open('../data/test.json', 'r') as f:
        data = json.load(f)
        return data

def parse_json_obj(resp_obj):
    try:
        resp_body = resp_obj.json()
    except ValueError:
        resp_body = resp_obj.text

    return {
        'status_code' : resp_obj.status_code,
        'headers' : resp_obj.headers,
        'body' : resp_body
    }

def get_cookie():
    pass

# 获取工作表
def get_sheet(file_path, sheet_name=''):
    workbook = load_workbook(file_path)
    ws = workbook[sheet_name]
    return ws

# 获取工作表某一行，并返回数组
def get_row_data(ws, row_num):
    rows = ws.rows
    row_data = []
    for row in list(rows)[row_num]:
        row_data.append(row.value)
    return row_data

def diff_content(resp_obj, expected_json):
    diff_json = {}
    resp_json = parse_json_obj(resp_obj)
    print resp_json
    print expected_json
    for key,expected_value in expected_json.items():
        resp_value = resp_json.get(key)
        if str(resp_value) != str(expected_value):
            diff_json[key] = {
                key : resp_value,
                "expected_value" : expected_value
            }

    return diff_json

def run_test_case(test_json):
    req_json = test_json['request']