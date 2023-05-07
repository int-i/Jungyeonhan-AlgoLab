def prime_list(m, n):
    if n < 2:
        return []

    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    eratos = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i <= sqrt(n)까지 검사
    lim = int(n**0.5)

    for i in range(2, lim + 1):
        if eratos[i] == True:  # i가 소수인 경우
            for j in range(i * 2, n, i):  # i 이후 i의 배수들을 False 판정
                eratos[j] = False

    # 소수 목록 산출
    return [i for i in range(max(m, 2), n) if eratos[i] == True]


M = int(input())
N = int(input())

primes = prime_list(M, N + 1)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)