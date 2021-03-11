a = 0
if a < 3:
    while True:
         username = input("请输入用户名：")
         password = input("请输入密码：")
         if username == "z" and password == "z":
             print("登陆成功")
             break
         else:
             print("用户名或密码输入错误。")
             a += 1
             print("即将进入判断的错误次数：", a)
         if  a > 3:
             print("您的密码已经输入错误三次。")
             open("z", 'w').write(str(a))
             break
else:
     print("该用户已锁定")
