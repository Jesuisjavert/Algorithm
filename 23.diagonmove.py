dx = [1, -1, -1, -1]
dy = [1, 1, -1, 1]
w, h = map(int, input().split())
x, y = map(int, input().split())
mode = 0
def isWall(x, y):
    if x>=0 and x<=w and y>=0 and y<=h:
        return True
    else: return False
for i in range(8):
    while(not isWall(x+dx[mode], y+dy[mode])):
        mode = (mode+1) % 4
    x += dx[mode]
    y += dy[mode]
    print(x, y)