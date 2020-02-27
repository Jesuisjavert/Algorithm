import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    result = []
    for x in range(N):
        for y in range(N):
            if arr[x][y]:   
                startx,starty = x, y
                while startx+1<N and arr[startx+1][y]:
                    startx+=1
                while starty+1<N and arr[x][starty+1]:
                    starty+=1
                finalx = startx+1-x
                finaly = starty+1-y
                result += [[finalx*finaly, finalx, finaly]]
                for a in range(x,startx+1):
                    for b in range(y,starty+1):
                        arr[a][b] = 0
    result.sort()
    print('#{} {}'.format(testcase,len(result)),end = "")
    for i in range(len(result)):
        print('',end=" ")
        print(*result[i][1:],end="")
    print()
