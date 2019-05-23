# -*- coding: utf-8 -*-
__author__ = "Lee.li"

import unittest
from airtest.core.api import *
from Script.skill import Skill
from multi_processframe.Tools import initial, screenshot


def Main(devices):
    class TCSkillProf4(unittest.TestCase):
        u'''测试用例以下为牧师分支的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            pass

        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            initial.startgame(devices)

        def test_Prof1_15(self):
            """
            这是测试Prof4-转职为牧师分支、祭祀分支、雷神分支
            return:
            """
            print("测试Prof4-转职为牧师分支、祭祀分支、雷神分支")
            self.assertEqual("雷神", Skill.test_Prof1_15(devices))
            screenshot.get_screen_shot(time.time(), devices, "牧师角色技能测试脚本")

        def test_Prof1_16(self):
            """
             Prof4-转职为牧师分支、祭祀分支、圣徒分支
            return:
            """
            print("测试Prof4-转职为牧师分支、祭祀分支、圣徒分支")
            self.assertEqual("圣徒", Skill.test_Prof1_16(devices))
            screenshot.get_screen_shot(time.time(), devices, "牧师角色技能测试脚本")

        def test_Prof1_17(self):
            """
            这是测试Prof4-转职为牧师分支、贤者分支、十字军分支
            return:
            """
            print("测试Prof4-转职为牧师分支、祭祀分支、十字军分支")
            self.assertEqual("十字军", Skill.test_Prof1_17(devices))
            screenshot.get_screen_shot(time.time(), devices, "牧师角色技能测试脚本")

        def test_Prof1_18(self):
            """
            这是测试Prof4-转职为牧师分支、贤者分支、圣骑士分支
            return:
            """
            print("测试Prof4-转职为牧师分支、祭祀分支、圣骑士分支")
            self.assertEqual("圣骑士", Skill.test_Prof1_18(devices))
            screenshot.get_screen_shot(time.time(), devices, "牧师角色技能测试脚本")


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print(f"{devices}结束运行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TCSkillProf4)
    return srcSuite
