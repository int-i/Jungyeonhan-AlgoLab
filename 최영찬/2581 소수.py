M = int(input())
N = int(input())

prime_sum = 0
min_prime = 10000

for i in range(M, N + 1):
    prime = True
    if i < 2:
        prime = False
    else:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
    if prime:
        if min_prime>i:
            min_prime = i
        prime_sum += i
if prime_sum == 0:
    print(-1)
else:
    print(prime_sum)
    print(min_prime)
