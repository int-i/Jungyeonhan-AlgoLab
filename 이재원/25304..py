X = int(input())
N = int(input())
t_list = []
for i in range(N):
    a, b = map(int,input().split())
    t = a*b
    t_list.append(t)
S = sum(t_list)
if X==S:
    print("Yes")
else:
    print("No")