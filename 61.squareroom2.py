def f(si, sj):
    q = [(si, sj)]
    cnt = 0
    while q:
        i, j = q.pop()
        cnt += 1
        for di, dj in (-1, 0), (1, 0), (0, 1), (0, -1):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if A[ni][nj] == A[i][j] + 1:
                    q.append((ni, nj))
    return cnt
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
 
    maxV = 0
    room = N**2
    for i in range(N):
        for j in range(N):
            result = f(i, j)
            if maxV < result:
                maxV = result
                room = A[i][j]
            elif result == maxV and A[i][j] < room:
                maxV = result
                room = A[i][j]
 
    print('#{} {} {}' .format(tc, room, maxV))