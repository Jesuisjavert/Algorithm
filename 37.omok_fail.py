import sys
sys.stdin = open('input.txt','r')
dx = [1,1,1,0]
dy = [1,0,-1,1]

def safe(x,y):
    global arr
    if 0<=x<19 and 0<=y<19:
        return True
    else:
        return False
def chutdol(x,y):
    if arr[x][y]==1 or arr[x][y]==2:
        color=arr[x][y]
        for search in range(4):
            nx=x+dx[search]
            ny=y+dy[search]
            if safe(nx,ny) and arr[nx][ny]==color:
                if safe(x-dx[search],y-dy[search]):
                    if arr[x-dx[search]][y-dy[search]]!=0:
                        return x,y
    pass

def omok(x, y):
    global arr
    for search in range(4):
        sx = x + dx[search]
        sy = y + dy[search]
        while safe(sx,sy) and arr[sx][sy]!=0:
            cnt = 1
            color = arr[sx][sy]
            sx += dx[search]
            sy += dy[search]
            cnt +=1
            if cnt == 5:
                answer[0] = color
                answer[1] = x+1
                answer[2] = y+1
answer = [0,0,0]
arr=[list(map(int,input().split())) for i in range(19)]
for x in range(19):
    for y in range(19):
        if safe(x,y):
            chutdol(x,y)
            omok(x,y)
print(answer)