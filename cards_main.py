#! /usr/bin/python3
# #!表示添加sheban标记,可以直接启动这个程序
import cards_tools

while True:
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作")
    print("您选择的操作是[%s]" % action_str)

    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
            pass
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
            pass
        # 查询名片
        else:
            cards_tools.search_card()
            pass
        pass
    elif action_str == "0":
        print("欢迎再次使用名片管理系统")
        # 如果在开发程序时,不希望立刻编写分支nebula的代码
        # 可以使用pass关键字,表示一个占位符
        # pass关键字不会执行任何的操作
        # TODO 针对找到的名片做修改和删除的操作
        break
    else:
        print("您输入的不正确,请重新输入")
