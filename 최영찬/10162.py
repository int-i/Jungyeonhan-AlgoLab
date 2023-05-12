time = int(input())
a = 300
b = 60
c = 10
aa = time // a
bb = (time % a) // b
cc= ((time % a) % b) //c

if (time % c) != 0:
    print(-1)
else:
    print(aa, bb, cc)