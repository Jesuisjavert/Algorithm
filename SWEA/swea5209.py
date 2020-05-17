def dfs(idx, pay):
    global minV
    global chk
    if idx==N:
        if minV>pay:
            minV = pay
            return
    for i in range(0, N):
        if(chk[i]==0):
            chk[i] = 1
            dfs(idx+1, pay+arr[idx][i])
            chk[i] = 0
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    minV = 100000000
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chk = [0 for _ in range(N)]
    dfs(0,0)
    print("#{} {}".format(tc, minV))