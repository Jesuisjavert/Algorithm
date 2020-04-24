# import sys
# sys.stdin = open('input.txt','r')
arr=[[0]*100 for _ in range(100)]
N= int(input())
for tc in range(N):
    startx, starty= map(int,input().split())
    for a in range(startx,startx+10):
        for b in range(starty,starty+10):
            arr[a][b]+=1
cnt=0
for x in range(100):
    for y in range(100):
        if arr[x][y]>0:
            cnt+=1
print(cnt)