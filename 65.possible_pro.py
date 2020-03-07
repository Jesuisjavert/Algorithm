import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = list(map(int, input().split()))
    ans=set([0])
    for x in p:
        num = set()
        for y in ans:
            num.add(x+y)
        ans = set(list(ans)+list(num))
    print('#{} {}'.format(tc, len(set(ans))))