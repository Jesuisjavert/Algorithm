import sys
sys.stdin = open("input.txt", "r")
for test_case in range(1, 11):
    T = int(input())
    arr=[list(map(int, input().split())) for i in range(100)]
    X = 0
    MIN = 99999
    cntlist = []
    for j in range(100):
        if arr[0][j] == 1:
            x = j
            cnt = 0
        for i in range(100):
            if x != 0 and arr[i][x-1] == 1:
                while x != 0 and arr[i][x - 1] == 1:
                    x -= 1
                    cnt += 1
            elif x < 99 and arr[i][x+1] == 1:
                while x != 99 and arr[i][x+1] == 1:
                    x += 1
                    cnt += 1
        if cnt <= MIN:
            res = j
            MIN = cnt
    print('#{} {}'.format(test_case, res))