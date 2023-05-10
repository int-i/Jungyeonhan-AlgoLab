a,b,c,d=map(int,input().split())
s = [a,b,c,d]
f,g,h,i=map(int,input().split())
t = [f,g,h,i]
if sum(s)<sum(t):
    print(sum(t))
elif sum(s)==sum(t):
    print(sum(s))
else:
    print(sum(s))