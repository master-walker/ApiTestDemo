#!/usr/bin/env python
# coding=utf-8

import ConfigParser
import sys, os
import codecs

src_path = os.path.abspath('..')
sys.path.append(src_path)
reload(sys)

# src目录
base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))
# 配置文件目录
config_path = os.path.join(base_path, 'config', 'conf.ini')


class ReadConfig(object):
    def __init__(self, path=config_path):
        config = ConfigParser.ConfigParser()
        # 读取配置文件
        config.readfp(codecs.open(path, 'r', 'utf-8-sig'))

        # 日志文件路径
        self.log_path = os.path.join(base_path, 'config' , 'logConf.ini')

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



if __name__ != "__main__":
    config = ReadConfig()
