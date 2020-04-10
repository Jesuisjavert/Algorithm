from collections import deque
import sys
sys.stdin = open('input.txt','r')
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(M)]
    queue=deque()  
    queue.extend(arr[0][:])
    cnt=1
    Flag=False
    while cnt<M:
        for i in range(cnt*N):
            if queue[i]>arr[cnt][0]:
                Flag=True
                index=i
                break
        if Flag:
            for i in range(N-1,-1,-1):
                queue.insert(index,arr[cnt][i])
            cnt+=1
            Flag=False
        else:   
            queue.extend(arr[cnt][:])
            cnt=cnt+1
    length=len(queue)
    a = list(queue)
    a.reverse()
    print('#{}'.format(tc),*a[:10])