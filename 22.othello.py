dy = [-1,-1, -1,0, 0, 1, 1, 1 ]
dx = [0, 1, -1, 1, -1,1,0, -1]

def safe(y, x):
    global arr
    if(1<=y and y<=N and 1<=x and x<=N):
        if(arr[y][x]==0):return 0
        return 1
    return 0

def check(y, x, dol, d):
    #8방향을 검사하는데 범위안넘어가는지 잘체크
    global arr
    ty = y + dy[d]
    tx = x + dx[d]
    if(safe(ty, tx) and arr[ty][tx]!=dol):
        while(1):
            y = y+dy[d]
            x = x+dx[d]
            if(safe(y, x)==0):return 0
            if(safe(y, x)and arr[y][x]==dol):return 1
    else: return 0

def paint(y, x, dol, d):
    global arr
    while(1):
        y = y+dy[d]
        x = x+dx[d]
        if(arr[y][x]==dol):break
        arr[y][x] = dol
    return

T = int(input())
for t in range(1, T+1):
    arr = [[0 for _ in range(10)] for _ in range(10)]
    N, M = map(int, input().split())
    d = N//2
    arr[d][d] = 2
    arr[d][d+1] = 1
    arr[d+1][d] = 1
    arr[d+1][d+1] = 2

    while(M):
        y, x, dol = map(int, input().split())
        #돌을 놓기전에 놓을 수 있는 칸인지 검사한다.
        #돌을 놓고나면 색상을 체인지 해준다.
        if(arr[y][x]==0):
            for i in range(0,8):
                if(check(y, x, dol, i)):
                    paint(y, x, dol, i)
                    arr[y][x] = dol
        M-=1

    W = 0
    B = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if(arr[i][j]==1):B+=1
            elif(arr[i][j]==2):W+=1

    print("#%d %d %d"%(t, B, W))