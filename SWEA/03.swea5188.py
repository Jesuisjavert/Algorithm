import sys
sys.stdin = open('input.txt','r')

def find(r, c, s):
    global minV
    if r==N-1 and c==N-1:
        if minV>s+m[r][c]:
            minV = s+m[r][c]
    else:
        if r+1<N:
            find(r+1,c,s+m[r][c])
        if c+1<N:
            find(r, c+1, s+m[r][c])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    minV = 100000
    find(0,0,0)
    print('#{} {}'.format(tc, minV))