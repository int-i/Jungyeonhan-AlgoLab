N,M=map(int,input().split())
card=list(map(int,input().split()))
li=[]
for i in range(N-2):
    fir=card[i]
    for j in range(i+1,N-1):
        sec=card[j]
        for k in range(j+1,N):
            thi=card[k]
            if fir+sec+thi > M:
                su=0
            else:
                su=fir+sec+thi
                li.append(su)
print(max(li))



