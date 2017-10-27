#!/usr/bin/env python
#coding=utf-8

'''

test

'''

import unittest
import multiprocessing
import time
from api import api_server


class ApiServerUnittest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.api_server_process = multiprocessing.Process(
            target = api_server.app.run()
        )
        cls.api_server_process.start()
        time.sleep(0.1)


    def tearDown(cls):
        cls.api_server_process.terminate()
