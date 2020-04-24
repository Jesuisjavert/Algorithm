def findsort():
    midmax = 0
    for a in price:
        if a > midmax:
            midmax = a
            if a== price[-1] and price[-2]<price[-1]:
                highpoint.append(a)
        if a < midmax:
            highpoint.append(midmax)
            midmax=0

import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,5):
    N = int(input())
    price = list(map(int, input().split()))
    highpoint = []
    findsort()
    minilist = []
    cnt = 0
    highpointcnt = 0
    finalresult = 0
    print(highpoint)
    while cnt != len(price) and highpointcnt != len(highpoint):
        if price[cnt]<highpoint[highpointcnt]:
            minilist.append(price[cnt])
            cnt +=1
        elif price[cnt]>highpoint[highpointcnt]:
            cnt+=1
        elif price[cnt]==highpoint[highpointcnt]:
            finalresult += ((len(minilist)*highpoint[highpointcnt])-sum(minilist))
            cnt+=1
            highpointcnt+=1
            minilist=[]
    print(finalresult)
