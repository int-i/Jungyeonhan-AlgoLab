n, m = map(int, input().split())

baskets = [0] * n  # 초기화

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        baskets[idx] = k  # i번째부터 j번째까지 k개의 공을 넣는다

for basket in baskets:
    print(basket, end=' ')