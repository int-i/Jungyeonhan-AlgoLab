li=[]
num=list(map(int,input().split()))
count=0
i = min(num)
while True:
    for j in range(5):
        if i%num[j]==0:
            count+=1
    if count>=3:
        li.append(i)
        break
    count=0
    i+=1

print(min(li))


