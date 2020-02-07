import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[int(x) for x in input().split()] for y in range(N)]
    cnt = 0
    for i in range(len(arr)):
        garo = 0
        for j in range(len(arr[i])):
            garo += arr[i][j]
            if arr[i][j] == 0:
                garo = 0
            if garo == M:
                cnt += 1
            if garo > M:
                cnt -= 1
                garo=0
    for p in range(len(arr[0])):
        sero = 0
        for q in range(len(arr)):
            sero += arr[q][p]
            if arr[q][p] == 0:
                sero = 0
            if sero == M:
                cnt += 1
            if sero > M:
                cnt -= 1
                sero =0
    print('#{}'.format(test_case),(cnt))