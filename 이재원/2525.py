A, B = map(int, input().split())
C = int(input())
M = C + B
if M > 60:
    A = A + 1 if A < 23 else 0
    M = M - 60
elif M == 60:
    A = A + 1 if A < 23 else 0
    M = 0
else:
    A = A
    M = M
print(A)
print(M)
