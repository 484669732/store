info = {
    "苹果":32.8,
    "香蕉": 22,
    "葡萄": 15.5
}
name = input("请输入需要查询金额的名称：")
if name in info :
    print(info[name])