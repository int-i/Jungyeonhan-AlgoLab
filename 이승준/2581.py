M=int(input())
N=int(input())
sosu=[]
for i in range(M, N + 1):
    if i != 1:
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count = 1
            if count == 1:
                break
        if count == 0:
            sosu.append(i)
if len(sosu)==0:
    print(-1)
else:
    print(sum(sosu))
    print(sosu[0])

