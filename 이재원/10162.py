T = int(input())
A, B, C = 300, 60, 10

if T % C != 0:
    print(-1)
else:
    n = T // A
    T %= A
    m = T // B
    T %= B
    s = T // C
    print(n, m, s)





T = int(input())
A, B, C = 300, 60, 10
p, q, r = map(int, input().split())

if p<=0 or q<=0 or r<=0:
    print(-1)
elif p*A+q*B+r*C < T:
    print(-1)
elif p*A+q*B+r*C == T:
    n = T//A
    T %= A
    m = T//(q*B)
    T %= q*B
    s = T//(r*C)
    print(n, m, s)
else:
    print(-1)