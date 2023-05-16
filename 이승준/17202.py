a=list((input()))
b=list((input()))
summ=[0]*17
for i in range(8):
    summ[2*i]=a[i]
    summ[2*i+1]=b[i]
for i in range(0,14):
    for n in range(0,15-i):
        summ[n]=int(summ[n])+int(summ[n+1])
        summ[n]=summ[n]%10
    summ[15-i]=0
print(str(summ[0])+str(summ[1]))


