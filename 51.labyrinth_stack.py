import sys
sys.stdin = open('input.txt','r')
def safe(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False
dx = [-1,0,1,0] #상우하좌
dy = [0,1,0,-1]
T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for a in range(N)]
    startx = 0
    starty = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 2:
                startx = x
                starty = y            
                break
    stack = []
    stack.append((startx,starty))
    result = 0
    while stack:
        t = stack.pop()
        if arr[t[0]][t[1]]== 3:
            result = 1
            break
        arr[t[0]][t[1]] = 1
        for direction in range(4):
            pathx = t[0]+dx[direction]
            pathy = t[1]+dy[direction]
            if safe(pathx,pathy) :
                if arr[pathx][pathy] in [0,3]:
                    future = (pathx,pathy)
                    stack.append(future)
                    if arr[future[0]][future[1]] == 3:
                        break
    print('#{}'.format(testcase),result)
                            


                    
