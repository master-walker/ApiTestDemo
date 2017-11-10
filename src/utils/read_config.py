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

        # api url
        self.url = config.get("Api", "url")
        # 登录数据
        self.username = config.get("login-data", "username")
        self.password = config.get("login-data", "password")
        # 发送邮件配置数据
        self.mail_host = config.get("Email", "mail_host")
        self.mail_user = config.get("Email", "mail_user")
        self.mail_password = config.get("Email", "mail_password")
        self.mail_port = config.get("Email", "mail_port")
        self.receiver = config.get("Email", 'receiver')
        self.subject = config.get("Email", "subject")



if __name__ == "__main__":
    ReadConfig = ReadConfig()
