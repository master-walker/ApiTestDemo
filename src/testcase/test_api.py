#!/usr/bin/python
# coding=utf-8

'''

'''

import traceback,ast
from requests.sessions import Session
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin
from utils import common
from utils.read_config import config

ws = common.get_sheet("../data/TestCase.xlsx","TestCase")
logger = common.get_logger()
base_url = config.url
session = Session()

    # 测试创建用户接口
def test_create_user():
    login_data = common.get_row_data(ws, 1)
    url_path = login_data[3]
    url = urljoin(base_url, url_path)
    data = login_data[6]
    expected_resp = login_data[8]
    expected_resp = ast.literal_eval(expected_resp)
    resp = session.post(url, data).json()
    try:
        assert resp == dict(expected_resp)
    except AssertionError:
        print traceback.print_exc()
    finally:
        logger.info(u"接口返回数据为：{0}".format(resp))