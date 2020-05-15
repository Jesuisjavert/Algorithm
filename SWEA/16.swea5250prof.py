import sys
sys.stdin = open('input.txt','r')

def cal(curX, curY):
    q.append((curX, curY))
    dBRD[0][0] = 0
    while q:
        curX, curY = q.pop(0)

        for dx, dy in [(-1, 0), (1,0), (0,-1), (0,1)]:
            tx = curX + dx
            ty = curY + dy
            if tx>=0 and tx<N and ty>=0 and ty < N :
                dif = 1
                if BRD[ty][tx] > BRD[curY][curX]:
                    dif += BRD[ty][tx] - BRD[curY][curX]
                if dBRD[ty][tx] > dBRD[curY][curX] + dif:
                    dBRD[ty][tx] = dBRD[curY][curX] + dif
                    q.append((tx, ty))

    return
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    BRD = [list(map(int, input().split())) for _ in range(N)]
    dBRD = [[100000]*N for i in range(N)]
    q = []
    cal(0,0)
    print('#{} {}'.format(tc, dBRD[N-1][N-1]))


