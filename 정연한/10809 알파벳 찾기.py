S = input()

# 알파벳과 해당 위치를 저장하는 딕셔너리 생성
pos = {chr(alpha): -1 for alpha in range(ord('a'), ord('z') + 1)}

# 입력 문자열을 순회하면서 각 알파벳이 처음 등장하는 위치를 딕셔너리에 저장
for i, ch in enumerate(S):
    if pos[ch] == -1:
        pos[ch] = i

# 딕셔너리의 값들을 출력
print(*pos.values())