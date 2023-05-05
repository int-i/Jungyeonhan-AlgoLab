N,M = map(int,input().split())
for M in range(M):
    i,j,k = map(int,input().split())

for N in range(N):
    list[N]=0

for M in range(M):
    while not i == j:
        list[i] = k
        i += 1

see=list
print(see)

