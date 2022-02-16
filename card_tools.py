def show_meun():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("4. 退出系统")
    print("*" * 50)


card_list = []


def add_card():
    name_str = input("请输入你的姓名")
    qq_str = input("请输入你的QQ")
    phone_str = input("请输入你的电话")
    mail_str = input("请输入你的邮箱")
    card_dict = {
        "name": name_str,
        "qq": qq_str,
        "phone": phone_str,
        "mail": mail_str
    }
    card_list.append(card_dict)


def show_all():
    if len(card_list) == 0:
        print("还没有任何的名片呢，请增加")

        return
    print("name\t\tqq\t\tphone\t\tmail\t\t")
    print("*" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"], card_dict["qq"], card_dict["phone"], card_dict["mail"]))


# for else结合使用，只有在for都遍历完成之后，才会去执行else后面的语句。
def find_card():
    find_str = input("请输入你要查找的名字")
    for card_dict in card_list:
        if card_dict["name"] == find_str:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["qq"], card_dict["phone"], card_dict["mail"]))
            # else:
            #     print("很抱歉没有找到你要的名字")
            # TODO 针对找到的记录执行修改和删除的操作
            update_card(card_dict)
            # 加上这个结束循环，一般名字是唯一的，没必要全表查找。不加也行
            break
    else:
        print("sorry 没有找到你要的名字呢")


def update_card(select_value):
    print("-" * 50)
    print("请输入您想进行的操作[%d] 修改卡片。[%d] 删除卡片。[%d] 返回上一级菜单" % (1, 2, 0))
    card_num = input("您的选择是：")
    if card_num == '1':
        # 第一个版本--修改卡片的值，不输入时会被空替换
        # select_value["name"] = input("要需改的电话是")
        # select_value["qq"] = input("要修改的qq为：")
        # select_value["phone"] = input("要修改的phone:")
        # select_value["mail"] = input("要修改的mail:")

        # TODO 输入空时不改变
        # 第二个版本--输入为空时不改变card值
        select_value["name"] = alter_input_card(select_value["name"],input("要需改的电话是"))
        select_value["qq"] = alter_input_card(select_value["qq"],input("要修改的qq为："))
        select_value["phone"] = alter_input_card(select_value["phone"],input("要修改的phone:"))
        select_value["mail"] = alter_input_card(select_value["mail"],input("要修改的mail:"))

    elif card_num == '2':
        card_list.remove(select_value)

# 判断输入的是否是空，是则赋予原来的值，不是就替换输入的值


def alter_input_card(real_value,message_info):
    # card_info = input(message_info)
    if len(message_info) == 0:
        return real_value
    else:
        return message_info


