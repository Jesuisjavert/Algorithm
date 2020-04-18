import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for testcase in range(1, T + 1):
    N, M = map(int, input().split(' '))
    arr = [list(map(int, input().split())) for _ in range(N)]
    sumlist = []
    for x in range(N):
        for y in range(N):
            sum = 0
            for i in range(M):
                for j in range(M):
                    if 0<=x+i<N and 0<=y+j<N:
                        sum += arr[x+i][y+j]
            sumlist.append(sum)
    print('#{}'.format(testcase),max(sumlist))