a = int(input("a = "))

b = int(input("b = "))

c = int(input("c = "))

if a != b and b != c and a != c:

    print("不规则三角形")

elif a == b and b == c:

    print("等边三角形")

else:

    print("等腰三角形")