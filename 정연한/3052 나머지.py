remainder = [int(input()) % 42 for _ in range(10)]
table = [0] * 42

for i in remainder:
    table[i] += 1

# table의 값 중 i가 0보다 큰 값들의 합을 구한다.
print(sum(1 for i in table if i > 0))