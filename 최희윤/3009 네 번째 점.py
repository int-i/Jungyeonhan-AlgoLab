A,a=map(int,input().split())
B,b=map(int,input().split())
C,c=map(int,input().split())

if A==B:
    D=C
else:
    if B==C:
        D=A
    else:
        D=B

if a==b:
    d=c
else:
    if b==c:
        d=a
    else:
        d=b

print(D,d)