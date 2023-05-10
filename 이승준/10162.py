A,B,C=300,60,10
Acook,Bcook,Ccook=0,0,0
cook=int(input())
if cook%10==0:
    Acook=cook//A
    Bcook=(cook%A)//B
    Ccook=(cook%A)%B//C
    print(Acook,Bcook,Ccook)
else:
    print(-1)

