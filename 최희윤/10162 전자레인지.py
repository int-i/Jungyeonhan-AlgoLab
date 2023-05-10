T=int(input())
l=[]
li=[300,60,10]

for i in li:
    count = T//i
    l.append(count)
    T %= i

if T==0:
    print(' '.join(map(str, l)))
else:
    print(-1)







