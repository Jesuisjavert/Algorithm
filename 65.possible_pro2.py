import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = list(map(int, input().split()))
    total = sum(p)
    s = [0]*(total+1)
    s[0] = 1
    for x in p:
        for i in range(total-x, -1,-1):
            if s[i]==1:
                s[i+x]=1
    print('#{} {}'.format(tc,sum(s)))