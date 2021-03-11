deep = 20
skip = 3
slide = 2
day = 0
while 1:
    deep -= skip
    if deep < 0:
        break
    deep += slide
    day += 1
print("天数:",day)

