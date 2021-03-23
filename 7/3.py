import pymysql
con = pymysql.connect(host="localhost",user="root",password="",database="bank")
cursor = con.cursor()
sql = "select * from yh"
cursor.execute(sql)
data = cursor.fetchall()
print(data)
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
        if a in data[0]:
            print("对")
            b = input("请输入密码：")
            if b == data[0][2]:
                print("对")
                c = input("请输入转入用户：")
                for i in range(2):
                    if c == data[i][0]:
                        print("对")
                        d = input("请选择转入金额:")
                        d = int(d)
                        sql = "select ye from yh where zh = %s"
                        cursor.execute(sql,a)
                        zx = cursor.fetchall()
                        zx = zx[0][0]
                        print(zx)
                        if d <= zx:
                            sql = "update yh set  ye = ye - %s  where zh = %s"
                            cursor.execute(sql,[d,a])
                            sql = "update yh set  ye = ye + %s  where zh = %s"
                            cursor.execute(sql,[d,c])
                            sql = "select ye from yh where zh = %s"
                            cursor.execute(sql,a)
                            a = cursor.fetchall()
                            con.commit()
                            print("转账成功","当前余额",a)
                            return 0
                        else:
                            print("转不了")
                            return 3
                    else:
                        if i == len(data):
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
cursor.close()
con.close()





