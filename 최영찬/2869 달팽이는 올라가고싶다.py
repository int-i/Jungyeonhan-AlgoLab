A, B, V = map(int, input().split())
togo = V-B
oneday=A-B
days = togo/oneday

if days == int(days):
    print(int(days))
else:
    print(int(days) + 1)
