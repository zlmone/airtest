
# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import equip
from multi_processframe.Tools import initial, screenshot

def Main(devices):
    class TC_equipv(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_guild(self):
            """
            装备-冒烟测试
            """
            try:
                print("开始测试装备相关模块")
                self.assertEqual("角色", equip.equip(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "装备-冒烟测试")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_equipv)
    return srcSuite
