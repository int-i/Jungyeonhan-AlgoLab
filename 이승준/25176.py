N=int(input())
def chung(N):
    if N>0:
        R=N*chung(N-1)
        return R
    else:
        return 1
print(chung(N))