s = {"苹果":12.3,"草莓":4.5,"香蕉":6.3,"葡萄":5.8,"橘子":6.4,"樱桃":15.8}
sum = 0
while 1:
    a = input("请输入购买物品：")
    if a =='q':
        break
    x = int(input("请输入购买数量："))
    b = s[a]
    sum = sum +b*x
print(sum)