import sys
sys.stdin = open('input.txt','r')
dx = [-1,0,1,0]   #상우하좌
dy = [0,1,0,-1]
def find3():
    stack = []
    stack.append([startj,starti])
    while True:
        if stack==[]:
            return 0
        x,y=stack.pop()
        arr[y][x]=5
        for i in range(len(dx)):
            if arr[y+dy[i]][x+dx[i]] == 3:
                return 1
            elif arr[y+dy[i]][x+dx[i]]==0:
                stack.append([x+dx[i],y+dy[i]])

for testcase in range(1, 11):
    input()
    arr = [list(map(int,input())) for a in range(16)]
    starti,startj = 1,1
    result=find3()

    print('#{} {}'.format(testcase,result))