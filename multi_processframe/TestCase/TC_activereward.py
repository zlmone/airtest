# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.smoking import active_reward
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TC_active_reward(unittest.TestCase):
        u'''测试用例102的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_sprite(self):
            """
            活跃奖励功能测试模块--主要检测每个界面按钮元素是否存在以及是否可点击
            """
            try:
                self.assertEqual("Duck", active_reward.active(devices))
            finally:
                screenshot.get_screen_shot(time.time(), devices, "活跃奖励模块功能测试脚本")

        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC_active_reward)
    return srcSuite