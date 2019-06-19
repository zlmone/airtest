# -*- encoding=utf8 -*-
__author__ = "Lee.li"
from airtest.core.api import *
from multi_processframe.Tools import screenshot, printcolor, adb_connect

def bag_item(devices):
    poco = adb_connect.device(devices)
    check_menu("SysAItem", poco) # 进入角色
    if poco("XSys_Bag_Item").exists(): # 进入龙器页签
        poco("XSys_Bag_Item").click()
        with poco.freeze() as freeze_poco:
            if freeze_poco(texture="l_zl").exists() and \
                    freeze_poco("PowerPoint").exists() and \
                    freeze_poco("ItemNewDlg(Clone)").offspring("item0").exists() and \
                    freeze_poco("ItemNewDlg(Clone)").offspring("item1").exists() and \
                    freeze_poco("ItemNewDlg(Clone)").offspring("item2").exists() and \
                    freeze_poco("ItemNewDlg(Clone)").offspring("item3").exists() and \
                    freeze_poco("DragObj").exists() and \
                    freeze_poco("add").exists() and \
                    freeze_poco("BagNum").exists():
                printcolor.printgreen("战力，背包分类，背包扩展UI元素显示正常")
            else:
                printcolor.printred("背包界面UI元素显示异常，详情见截图")
                screenshot.get_screen_shot(time.time(), devices, "背包界面UI元素显示异常")
            try:
                with poco.freeze() as freeze_poco:
                    countbegin = int(poco("BagNum").get_text().split("/", 1)[1])
                    freeze_poco("ItemNewDlg(Clone)").offspring("item0").offspring("TextLabel").click()
                    freeze_poco("ItemNewDlg(Clone)").offspring("item1").click()
                    freeze_poco("ItemNewDlg(Clone)").offspring("item2").click()
                    freeze_poco("ItemNewDlg(Clone)").offspring("item3").click()
                    freeze_poco("add").click()
                    number = int(poco("GreyModalDlg(Clone)").offspring("Bg").child("Label").get_text()[4:7].split("个")[0]) # 获取需要几个背包扩充券
                    poco("OK").click()
                    poco("ListPanel").click()
                    for i in range(number+2):
                        poco("OK").click()
                    poco("Close").click()
                    freeze_poco("add").click()
                    poco("OK").click()
                    countend = int(poco("BagNum").get_text().split("/", 1)[1])
                    if (countend-countbegin) == 5:
                        printcolor.printgreen("背包扩充成功")
                    else:
                        printcolor.printred("背包扩充失败")
                printcolor.printgreen("背包按钮点击正常")
            except Exception as e:
                printcolor.printred("背包按钮点击异常")
                printcolor.printred(e)
                screenshot.get_screen_shot(time.time(), devices, "背包按钮点击异常")
    else:
        printcolor.printred("背包功能暂未开放，请提升等级角色")
        screenshot.get_screen_shot(time.time(), devices, "背包功能暂未开放")
    poco("Close").click()
    return poco("Duck").get_name()   # 返回值poco("Duck").get_name()

def check_menu(sysmenu, poco):
    position = poco(sysmenu).get_position()
    if position[0] > 1:  # 对比pos点，得到的pos列表中，第一个元素 > 1 说明在屏幕外面
        poco("MenuSwitchBtn").click()
        time.sleep(1)
        poco(sysmenu).click()
    else:
        poco(sysmenu).click()


# devices = "127.0.0.1:62001"
# bag_item(devices)