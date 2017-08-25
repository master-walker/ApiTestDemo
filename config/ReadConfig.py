#!/usr/bin/env python
# coding=utf-8

import ConfigParser
import sys, os

src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)


class ReadConfig(object):
    def __init__(self, path='.\conf.ini'):
        config = ConfigParser.ConfigParser()
        # 读取配置文件
        config.read(path)

        self.url = config.get("base", "url")
        self.username = config.get("login-data", "username")
        self.password = config.get("login-data", "password")


if __name__ == "__main__":
    ReadConfig = ReadConfig()
