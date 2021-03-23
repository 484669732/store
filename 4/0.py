shop = [
    ["Iphone 6x",6000],
    ["HUAWEI watch",2000],
    ["lenovo Pc",4500],
    ["Mac Pc",12000],
    ["卫龙辣条",5],
    ["老干妈",7.5]
]
salary = int(input("请输入您的初始资金："))
mycat = []
while True:
    for index, value in enumerate(shop):
        print(index, value)

    num = input("亲输入您要的商品编号：")

    if num.isdigit():
        # 0 ~ 5
        num = int(num)
        if num in range(len(shop)):#  3  0~5

            if salary >= shop[num][1]:

                mycat.append(shop[num])

                salary = salary - shop[num][1]
                print("\033[32;20;1m购买成功！您的余额为：",salary,"￥！\033[0m")
            else:
                print("\033[41;20;1m对不起，您的余额不支持买改商品！穷鬼！\033[0m")
        else:
            print("该商品不存在！别瞎弄！")
    elif num == "Q" or num == "q":
        print("欢迎下次光临！")
        break
    else:
        print("输入非法，请重新输入！")
print("您的购买内容为：")
for index,value in enumerate(mycat):
    print(index,":",value)
print("------------您的余额：",salary,"￥！------------------")
