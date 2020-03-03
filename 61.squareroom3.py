def dfs(i, j, leng):
    global prev
 
    visited[i][j] = True
 
    for mode in range(4):
        Y = i + dy[mode]
        X = j + dx[mode]
        if X < 0 or Y < 0 or X >= N or Y >= N: continue
        if grid[i][j] + 1 == grid[Y][X]:
            dfs(Y, X, leng + 1)
 
    if prev < leng:
        prev = leng
        cnt[grid[y][x]] = prev
 
 
for tc in range(1, int(input()) + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
 
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = [0] * (N ** 2)
    visited = [[False] * N for _ in range(N)]
 
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                prev = 0
                dfs(y, x, 0)
 
    print('#{} {} {}'.format(tc, cnt.index(max(cnt)), max(cnt) + 1))