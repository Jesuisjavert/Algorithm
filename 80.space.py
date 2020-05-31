import sys
sys.stdin = open('input.txt','r')
T = int(input())
arr = [[0]*100 for _ in range(100)]
for tc in range(1,T+1):
    startx, starty = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[startx+i][starty+j] += 1
cnt = 0
for a in range(100):
    for b in range(100):
        if arr[a][b] != 0:
            cnt+=1
print(cnt)
