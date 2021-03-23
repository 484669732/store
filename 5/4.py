names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
name = []
for i in range(len(names)):
    a = names[i][0]
    b = name.append(a)
print(name)
d = dict(zip(name,names))
print(d)