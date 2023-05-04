H,M=map(int, input().split())
h=H*60
t=h+M-45

if t<0:
    if M<45:
        print(23, 60+t)

else:
    print(t//60, t%60)
