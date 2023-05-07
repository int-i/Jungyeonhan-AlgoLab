N = int(input())
K = int(input())

res =0
for i in range(1, N+1):
    if N % i ==0:
        K = K-1
        if K == 0:
            res = i

print(res)