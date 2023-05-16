N=int(input())
li=[0]*(N+1)
li[1]=1
for i in range(2,N+1):
    li[i]=li[i-2]+li[i-1]
print(li[N])