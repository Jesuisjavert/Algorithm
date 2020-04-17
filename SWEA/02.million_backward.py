import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    price = list(map(int, input().split()))
    peak = 0
    money = 0
    for a in range(len(price)-1,-1,-1):
        if price[a]>peak:
            peak = price[a]
        if price[a]<peak:
            money += peak-price[a]
    print('#{} {}'.format(testcase,money))
