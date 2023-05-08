lvalue = set()

for i in range(10):
    num = int(input())
    value = num % 42
    lvalue.add(value)
count = len(lvalue)
print(count)