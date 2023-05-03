H,M=map(int, input().split())
C=int(input())

h=H*60
t=h+M+C

if t//60>=24:
    print(t//60-24, t%60)
else:
    print(t//60, t%60)