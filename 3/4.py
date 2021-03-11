b=[1,5,21,30,15,9,30,24]
a=0
z=0
while a <= 7:
     if b[a] % 5 == 0:
          z += b[a]
     a += 1
print(round(z,2),)