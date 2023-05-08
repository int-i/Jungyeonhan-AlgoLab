n, m = map(int, input().split())
cardlist = list(map(int, input().split()))
maximum = 0
for i in range(len(cardlist) - 2):
    for j in range(i+1, len(cardlist) - 1):
        for k in range(j+1, len(cardlist)):
            sum = cardlist[i] + cardlist[j] + cardlist[k]
            if sum <= m and sum > maximum:
                maximum = sum
print(maximum)
