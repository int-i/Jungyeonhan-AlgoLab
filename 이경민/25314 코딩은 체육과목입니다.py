#1330번
A,B = map(int,input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

'''
#25304번
total = int(input())

type = int(input())

sum = 0  

for i in range(type):
    a, b = map(int, input().split())
    sum += a * b

if total == sum:
    print("Yes")
else:
    print("No")
'''


