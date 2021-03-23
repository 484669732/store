from DBUtils import select
from DBUtils import update
class Bank:
    bankName = "中国工商银行账户管理系统"

    def  bank_AddUser(self,user):
        # 判断数据库是否已满
        sql1 = "select  count(*)  from q"
        data = select(sql1, [])
        if data[0][0] >= 100:  # 如果返回的统计数据超出100，则已满
            return 3
        # 判断数据是否存在改用户
        # 获取所有键，然后在判断是否有
        sql2 = "select * from q  where  id = %s"
        param2 = [user.getAccount()]
        data2 = select(sql2, param2)
        if len(data2) != 0:  # 如果通过sql语句能查到数据并且不为空，则说明改用户已存在
            return 2
        # 正常开户：insert into 表  ，否则则执行存储数据操作
        sql3 = "insert into q values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"  # now() 使用的mysql数据库自己的时间
        param3 = [user.getAccount(),
                  user.getUsername(),
                  user.getPassword(),
                  user.getAddress().getCountry(),
                  user.getAddress().getProvince(),
                  user.getAddress().getStreet(),
                  user.getAddress().getDoor(),
                  user.getMoney(),
                  self.bankName]
        update(sql3, param3)
        return 1


def zhuanzhang(self):
    zhanghu = input("账户")
    mima = input("密码")
    sql = "select *  from  yh  where  zh = %s and mm = %s"
    date = select(sql, [zhanghu, mima])
    if date == ():
        print("输入信息错误")
        return 1
    else:
        zhanghu1 = input("对方账户")
        sql1 = "select *  from  yh  where  zh = %s"
        date1 = select(sql1, [zhanghu1])
        if date1 == ():
            print("对方不在")
            return 3
        else:
            jine = input("给多少钱")
            sql4 = "select * from yh where zh = %s"
            date2 = select(sql4, zhanghu)
            jine1 = int(jine)
            if date2[0][7] < jine1:
                print("转不来")
            else:
                sql1 = "update yh set ye = ye - %s  where zh = %s"
                date = select(sql1, [jine,zhanghu])
                sql2 = "update yh set ye = ye + %s  where zh = %s"
                date = select(sql2, [jine,zhanghu1])

                sql3 = "select * from yh where zh = %s"
                date22 = select(sql3, zhanghu)
                print("余额",date22[0][7])


zhuanzhang(1)