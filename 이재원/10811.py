n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

def reverse_arr(start, end):
    for i in range((end-start+1)//2):
        arr[start+i], arr[end-i] = arr[end-i], arr[start+i]

for _ in range(m):
    i, j = map(int, input().split())
    reverse_arr(i-1, j-1)

print(' '.join(map(str, arr)))