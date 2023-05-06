maximum = 0
y = 0
x = 0

for i in range(9):  # 9개의 줄에 대해 반복
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > maximum:
            maximum = row[j]
            y = i + 1
            x = j + 1

print(maximum)
print(y, x)
