names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
    ]
avg=0
sum=0
for i in range(len(names)):
    j = names[i][5]
    sum = j + sum
avg = sum / len(names)
print(avg)