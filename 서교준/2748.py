n = int(input())
lis =[0, 1]
for i in range(2,n+1):
    lis.append(lis[i-1] + lis[i-2])
print(lis[n])
