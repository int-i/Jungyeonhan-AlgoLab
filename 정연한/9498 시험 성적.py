# 백준 채점 시 pypy3가 아니라 python 3로 해야 됨
# match-case문이 최신 문법이라 pypy3로 컴파일을 못함

score = int(input())

match score // 10:
    case 10:
        print('A')
    case 9:
        print('A')
    case 8:
        print('B')
    case 7:
        print('C')
    case 6:
        print('D')
    case _:
        print('F')