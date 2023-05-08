N, X = map(int, input().split())

A = [i for i in map(int, input().split()) if X > i]

print(*A)
