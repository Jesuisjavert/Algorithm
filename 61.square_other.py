def search(y, x, k):
    global ans, move
    v[y][x] = 1
    cnt = 0
    for d in range(4):
        if (y == 0 and d == 1) or (y == n-1 and d == 0) or (x == 0 and d == 3) or (x == n-1 and d == 2):
            cnt += 1
            continue
        if lst[y][x]-lst[y+dy[d]][x+dx[d]] == -1:
            search(y + dy[d], x + dx[d], k + 1)
            return
        else:
            cnt += 1
    if cnt == 4:
        if move == k:
            ans = lst[i][j] if ans > lst[i][j] else ans
        elif move < k:
            ans, move = lst[i][j], k
        return
 
 
T = int(input())
 
for tc in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    v = [[0]*n for _ in range(n)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    ans = 0
    move = 0
    for i in range(n):
        for j in range(n):
            k = 1
            if v[i][j]:
                continue
            search(i, j, k)
 
    print("#{} {} {}".format(tc+1, ans, move))