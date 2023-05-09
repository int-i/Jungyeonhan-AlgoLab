N,M = map(int,input().split())
li=[]
for N in range(N):
    li.append(N+1)

for M in range(M):
    i,j=map(int,input().split())
    a=li[i-1]
    b=li[j-1]
    li[i-1]=b
    li[j-1]=a

print(' '.join(map(str, li)))
