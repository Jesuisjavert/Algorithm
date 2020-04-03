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
    stage = 0
    finalstage=[]
    stack.append([startx,starty,stage])
    while stack:
        t = stack.pop(0)
        for direction in range(4):
            pathx = t[0]+dx[direction]
            pathy = t[1]+dy[direction]
            if safe(pathx,pathy) :
                if arr[pathx][pathy] == 0:
                    arr[pathx][pathy] = 1
                    future = [pathx,pathy,t[2]+1]
                    stack.append(future)
                elif arr[pathx][pathy] == 3:
                    finalstage.append(t[2])
                    break
    if finalstage==[]:
        finalstage.append(0)
    print('#{}'.format(testcase),min(finalstage))