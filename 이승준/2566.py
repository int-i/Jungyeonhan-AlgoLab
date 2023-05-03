li = [[int(i) for i in input().split()] for _ in range(9)]
max= 0
x=0
y=0
for i in range(9):
    for j in range(9):
        if li[i][j] > max:
            x=i
            y=j
            max=li[i][j]

print(max)
print(x+1,end = " ")
print(y+1)