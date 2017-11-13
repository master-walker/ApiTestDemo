#!/usr/bin/env python
# coding=utf-8

'''
utils function
'''
from openpyxl import load_workbook
import json,traceback
import logging
import smtplib,re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from utils.read_config import config
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

# 比较预期请求结果和实际结果
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

# 获取日志记录器
def get_logger():
    logging.config.fileConfig(config.log_path)
    logger = logging.getLogger()
    return logger

def _attach_file(att_file):
    """将单个文件添加到附件列表中"""
    att = MIMEText(open('%s' % att_file, 'r').read(), 'plain', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    file_name = re.split(r'[\\|/]', att_file)
    att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
    # msg.attach(att)
    # logger.info('attach file {}'.format(att_file))
    return att

# 发送邮件
def send_email(server, sender, password, receiver, subject, message=None, files=None):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # 邮件正文
    if message:
        msg.attach(MIMEText(message))

    # 构造附件
    # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
    if files:
        if isinstance(files, list):
            for f in files:
                msg.attach(_attach_file(f))
        elif isinstance(files, str):
            msg.attach(_attach_file(files))
    try:
        smtp_server = smtplib.SMTP(server)
    except (gaierror and error) as e:
        print '连接邮件服务器失败'
    else:
        try:
            smtp_server.login(sender, password)
        except smtplib.SMTPAuthenticationError as e:
            traceback.print_exc()
        else:
            smtp_server.sendmail(sender,receiver, msg.as_string())
        finally:
            smtp_server.quit()


def run_test_case(test_json):
    req_json = test_json['request']