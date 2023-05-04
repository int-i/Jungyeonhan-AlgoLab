puts = input()
split = puts.split()
A = int(split[0])
B = int(split[1])
if A > B:
    print('>')
if A < B:
    print('<')
if A == B:
    print('==')