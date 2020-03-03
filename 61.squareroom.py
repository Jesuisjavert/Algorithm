import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,3):
    N = int(input())
    arr = [list(map(int, input().split())) for a in range(N)]
    dx = [0,1,0,-1]   #상우하좌
    dy = [-1,0,1,0]
    cnt = 1
    move = []
    for x in range(N):
        for y in range(N):
            for direction in range(4):
                movex = x + dx[direction]
                movey = y + dy[direction]
                if 0<=movex<N and 0<=movey<N and abs(arr[x][y] - arr[movex][movey]==1):
                    cnt+=1
                    move.append(arr[x][y])
                else:
                    pass
    print(move,cnt)