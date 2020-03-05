import sys
sys.stdin = open('input.txt','r')

def rec(i, myset, total):
    global mxm
    if total <= mxm:
        return
    if i == n :
        mxm = total
    for k in range(n):
        if k not in myset and a[i][k] != 0:
            #print(i,k,a[i][k])
            rec(i+1,myset+[k], total * a[i][k] / 100)
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    a = [list(map(int, input().split()))for _ in range(n)]
    mxm = 0
    rec(0, [], 100)

    print('#{}'.format(tc), end=' ')
    print('%0.6f' % mxm)
#배열을 움직이는 방식이라 실행시간 오래걸림