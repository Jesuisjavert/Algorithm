import sys
sys.stdin = open('input.txt','r')

dx=[0,1,-1,0]
dy=[1,0,0,-1]
T=10
def find3():
    stack=[]
    stack.append([startj,starti])
    while True:
        if stack==[]:
            return 0
        x,y=stack.pop()
        bg[y][x]=5
        for i in range(len(dx)):
            if bg[y + dy[i]][x + dx[i]] == 3:
                return 1
            elif bg[y+dy[i]][x+dx[i]]==0:
                stack.append([x+dx[i],y+dy[i]])
                      
for t in range(1,T+1):
    input()
    bg=[ [int(x) for x in input()] for j in range(16) ]
    starti,startj=1,1
    result=find3()
 
    print('#{} {}'.format(t,result))