import sys; sys.stdin = open('input.txt','r')

dx= [-1, -1, -1, 0, 1,1,1,0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

for tc in range(1, int(input()) +1 ):
    N, M = map(int, input().split())

    #게임판의 상태를 저장
    pan = [[0] * (N+1) for _ in range(N+1)]
    #초기 게임판의 상태를 설정
    p = N //2
    pan[p][p] =  pan[p+1][p+1] = 2
    pan[p+1][p] = pan[p][p+1] = 1

    # M번의 돌을 두는 정보 처리
    for _ in range(M):
        x, y, dol = map(int, input().split())
        pan[x][y] = dol

        for i in range(8):
            tx, ty = x+dx[i],y+dy[i]

            while 1<= tx <= N and 1<= ty <= N:
                if pan[tx][ty] == 0: break
                if pan[tx][ty] == dol:
                    #tx, ty --> x, y
                    while tx != x or ty != y:
                        pan[tx][ty] = dol
                        tx, ty = tx-dx[i],ty-dy[i]
                        

                tx, ty= tx + dx[i], ty+dy[i]
