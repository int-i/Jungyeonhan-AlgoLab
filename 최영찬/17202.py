num1 = input()
num2 = input()
num1 = str(num1)
num2 = str(num2)
result = ""
for i in range(len(num1)):
    result += num1[i] + num2[i]
while len(result) > 2:
    cul = ""
    for i in range(len(result) - 1):
        cul += str((int(result[i]) + int(result[i + 1])) % 10)
    result = cul
print(result)
