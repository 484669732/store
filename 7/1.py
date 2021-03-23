import pymysql
con = pymysql.connect(host="localhost",user="root",password="",database="company")
cursor = con.cursor()
data = cursor.fetchall()
'''bank = {
        '35163969': {'username': '1',
                     'password': '1',
                     'country': '1',
                     'province': '1',
                     'street': '1',
                     'door': '1',
                     'money': 500,
                     'bank_name': '中国工商银行昌平区回龙观支行'},
        '35163968': {'username': '1',
                    'password': '1',
                    'country': '1',
                    'province': '1',
                    'street': '1',
                    'door': '1',
                    'money': 100,
                    'bank_name': '中国工商银行昌平区回龙观支行'},
}
'''
def sb(ab) :
    if ab == "4" :
        a = input("请输入户名；")
        if a in data:
            print("对")
            b = input("请输入密码：")
            if b == bank[a]['password']:
                print("对")
                c = input("请输入转入用户：")
                if c in bank.keys():
                    print("对")
                    d = input("请选择转入金额:")
                    d = int(d)
                    if d <= bank[a]['money']:
                        bank[a]['money'] = bank[a]['money'] - d
                        bank[c]['money'] = bank[c]['money'] + d
                        print("转账成功","当前余额",bank[a]['money'])
                        return 0
                    else:
                        print("转不了")
                        return 3
                else:
                    print("不存在")
                    return 1
            else:
                print("不正确")
                return 2
        else:
            print("不存在")
            return 1
    else:print("gun")
a =input("转账")
print(sb(a))





