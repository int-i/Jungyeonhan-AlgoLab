row = list(map(int, input().split()))
num=1
while True:
    count = 0
    for n in row:
        if num % n == 0:
            count += 1
    if count >= 3:
        break
    num += 1
print(num)
