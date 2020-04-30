import sys
sys.stdin = open('input.txt','r')

def dij():
    u.append(0)
    D[0] = 0
    curV = 0
    while len(u) <= N:
        for i in adj[curV]:
            w = adj[curV].get(i)
            if i in u:
                continue
            if D[i] > D[curV] + w:
                D[i] = D[curV] + w
        minV = 1000000
        for i in range(N+1):
            if i in u:
                continue
            if D[i] < minV:
                curV = i
                minV = D[i]
        u.append(curV)
    return

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [{} for i in range(N+1)]

    D = [10000000] * (N+1)
    u = []
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
    
    dij()
    print('#{}'.format(tc),D[N])