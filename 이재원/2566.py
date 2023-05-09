max_val = 0
max_row, max_col = 0, 0

for row in range(9):
    nums = list(map(int, input().split()))
    for col, num in enumerate(nums):
        if num > max_val:
            max_val = num
            max_row, max_col = row, col

print(max_val, max_row+1, max_col+1)
