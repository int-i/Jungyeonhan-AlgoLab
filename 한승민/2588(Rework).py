a = int(input())
b = int(input())
print (a*(b%10))
print (a*((b//10)%10))
print (a*((b//10)//10))
print (a*b)
# = 5번줄 print (a*((b//10)//10)) = (a*(b//100))같은 출력