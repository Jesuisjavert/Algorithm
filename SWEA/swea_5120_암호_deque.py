from collections import deque
import sys
sys.stdin = open('input.txt','r')

T=int(input())
for tc in range(1,T+1):
    N,M,K=map(int,input().split())

    que=deque()   ### que에 deque를 만들어준다.
    arr=list(map(int,input().split()))
    que.extend(arr)   ### 그리고 que에 arr를 넣어준다.
    ind=0   ## 탐색해야할 ind의 위치를 말해준다.
    while K:
        if ind+M<N:   ## 최초 탐색위치는 ind+M인데, 그게 전체 크기 N보다 작을때에는
            ind=ind+M   ### ind+M을 해준다.
            temp=que[ind]+que[ind-1]    #### 찾아야하는 ind와 그보다 작은값을 구하고,
            que.insert(ind,temp)       ### 그 ind에 temp를 넣어준다.
            N+=1                      ### 값이 추가 됬으면 전체크기도 늘어났으니 N+1 해준다.
        elif ind+M==N:              ### 만약 ind+M이 N하고 같으면, 새 암호의 위치가 가장끝에 위치하는것이여서
            ind=ind+M               
            temp=que[ind-1]+que[0]  ### 제일 앞의 값과 제일 끝의 값을 더해준다.
            que.append(temp)       ### 그리고 가장 끝에 그 값을 추가해준다.
            N+=1
        else:
            ind=ind+M-N          ### 그 외에는 앞으로 되돌아가는것이므로 N을 빼준다.
            temp=que[ind]+que[ind-1]   ### 그리고 그 위치의 값과 그 전값을 더해서 
            que.insert(ind,temp)      ### 해당 ind에 넣어준다.
            N+=1
        K-=1             ### 우리는 총 K번 하는것이므로 1번의 작업이 끝나면 1씩 줄여준다.
    a = list(que)
    a.reverse()
    print('#{}'.format(tc),*a[:10])