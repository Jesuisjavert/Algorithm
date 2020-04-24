dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #상 하 좌 우
arr = [[]]
N = 4
for x in range(N):
    for y in range(N):
        #arr[x][y]
        #상 하 좌 우
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            # 항상 경계체크가 필요하다.
            if 0 <= tx< N and 0<= ty < N:
            # tx, ty 에 대해서 작업을 한다.
            