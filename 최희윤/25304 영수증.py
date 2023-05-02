X = int(input())
N = int(input())
Sum = 0
for i in range(N):
    a, b = map(int, input().split())
    Sum = a * b
if X == Sum:
    print("Yes")
else:
    print("No")
