import sys 
import itertools
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):  
    N, height = map(int, input().split())
    jumwonkey=list(map(int, input().split()))
    # print(N, height, jumwonkey)
    sumlist = []
    for k in range(1,N+1):
        t=itertools.combinations(jumwonkey,k)    
        for i in t:
            temp=0
            for ttt in i:
                temp+=ttt
                if height<=temp<height+100:
                    sumlist.append(sum(i))
    resultlist = []
    for a in sumlist:
        resultlist.append(a - height)
    print('#{} {}'.format(testcase,min(resultlist)))