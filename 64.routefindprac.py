def find(i, j, n, s):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    if n == 7:
        t.add(s)
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni>=0 and ni<4 and nj>=0 and nj <4:
                find(ni, nj, n+1, s+ str(a[i][j]))
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    a = [list(map(int, input().split()))for _ in range(4)]
    t = set()
    for i in range(4):
        for j in range(4):
            find(i, j, 0, "")
    print('#{} {}'.format(tc,len(t)))