from collections import deque
import sys
sys.stdin = open('input.txt','r')
T=int(input())
for tc in range(1,T+1):
    N,M,K=map(int,input().split())
    queue=deque()
    arr=list(map(int,input().split()))
    queue.extend(arr)
    idx=0
    while K:
        if idx+M<N:
            idx=idx+M
            temp=queue[idx]+queue[idx-1]
            queue.insert(idx,temp)
            N+=1
        elif idx+M==N:
            idx=idx+M
            temp=queue[idx-1]+queue[0]
            queue.append(temp)
            N+=1
        else:
            idx=idx+M-N
            temp=queue[idx]+queue[idx-1]
            queue.insert(idx,temp)
            N+=1
        K-=1
    a = list(queue)
    a.reverse()
    print('#{}'.format(tc),*a[:10])