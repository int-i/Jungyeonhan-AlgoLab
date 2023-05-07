N, X = map(int, input().split())

numbers = input().split()

result = ""
for num in numbers:
    if int(num) < X:
        result += num + " "

print(result)
