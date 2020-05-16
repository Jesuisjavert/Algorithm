from collections import deque

direction = {(-1,0), (0,1), (1,0), (0,-1)}
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[int(x) for x in input()] for _ in range(N)]
    visited = [[1000]*N for _ in range(N)]

    Q = deque([(0,0,0)])
    while Q:
        i, j, cnt = Q.popleft()
        for d in direction:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] > cnt + arr[ni][nj]:
                    visited[ni][nj] = cnt + arr[ni][nj]
                    Q.append((ni,nj,cnt+arr[ni][nj]))

    print('#{}'.format(tc), visited[N-1][N-1])