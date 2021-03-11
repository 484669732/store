i = 1
j = 1
while i< 10:
    while j<(i+1):
        print("%d*%d=%d"%(j,i,i*j),end="\t")
        j=j+1
    print()
    i=i+1
    j=1
