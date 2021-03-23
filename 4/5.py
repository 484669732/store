li = [["罗恩", 23, 35, 44],
      ["哈利", 60, 77, 68, 88, 90],
      ["赫敏", 97, 99, 89, 91, 95, 90],
      ["马尔福", 100, 85, 90]]
for x in range(len(li)):
    num = 0
    for y in range(1, len(li[x])):
        num += li[x][y]
    print(li[x][0], "的成绩为", num)
