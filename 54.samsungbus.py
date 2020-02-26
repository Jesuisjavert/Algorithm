import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    cntlist = [0 for a in range(10000)]
    ABlist = []
    for i in range(N):
        A, B = map(int, input().split())
        ABlist.append([A,B])
        for one in range(A,B+1):
            cntlist[one] +=1
    printstation = []
    P = int(input())
    for a in range(P):
        a = int(input())
        printstation.append(cntlist[a])
    print('#{}'.format(testcase),*printstation)
