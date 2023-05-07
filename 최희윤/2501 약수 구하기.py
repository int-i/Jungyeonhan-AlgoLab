N,K=map(int,input().split())
li=list()
i=1

while not N==i:
    if N%i==0:
        li.append(i)
        i+=1
    else:
        i+=1

if len(li)<K:
    print(0)
else:
    print(li[K-1])