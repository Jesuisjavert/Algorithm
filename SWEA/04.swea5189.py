import sys
sys.stdin = open('input.txt','r')

# k은 순열의 인덱스, prek은 방문위치, s는 현재까지의 소모량
def find(k, prek, s):
    global minV
    if k == N:
        if minV > s:
            minV = s
            return
    elif k==N-1:
        find(k+1,1,s+brd[prek][0])
    else:
        visited[prek]=1
        if s>minV:
            return
        else:
            for i in range(N):
                if visited[i] ==0:
                    visited[i] = 1
                    find(k+1, i, s+brd[prek][i])
                    visited[i] = 0
        

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    brd = [list(map(int, input().split())) for x in range(N)]
    minV = 100000
    visited = [0 for i in range(N+1)]
    find(0,0,0)
    print('#{} {}'.format(tc, minV))