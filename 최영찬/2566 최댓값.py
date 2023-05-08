maximum1 = 0
y = 0
x = 0

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > maximum1:
            maximum1 = row[j]
            y = i + 1
            x = j + 1

print(maximum1)
print(y, x)
