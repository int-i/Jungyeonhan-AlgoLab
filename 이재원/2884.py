M, H = map(int,input().split())
if H<45:
    M = M-1 if M>0 else 23
    H = 60 - (45 - H) if H > 0 else 15
    print(M)
    print(H)
else:
    print(M)
    print(H-45)