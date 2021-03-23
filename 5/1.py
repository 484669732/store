dict = {"k1":"v1","k2":"v2","k3":"v3"}
for i in dict.keys() :
    print(i)
for i in dict.keys(): # 遍历dict  i = k1
    print(dict[i]) # i = k1
dict["k4"] = input("请输入：")
print(dict)
print(dict["k1"])
