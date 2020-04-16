import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int,input().split())
    TREE = [0 for _ in range(N+1)]
    for _ in range(M):
        idx, value = map(int, input().split())
        TREE[idx] = value
    
    n = N
    while n>1:
        TREE[n//2] += TREE[n]
        n -= 1
    result = TREE[L]
    print('#{} {}'.format(tc, result))