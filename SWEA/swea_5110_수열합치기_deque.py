from collections import deque


T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(M)]
    result=deque()  ### result를 deque로 설정해준다.
    result.extend(arr[0][:])   ### 그리고 가장 첫행을 extend로 result에 넣어준다.

    t=1
    Flag=False
    while t<M:

        for i in range(t*N):    #### 매번 N개의 list가 붙여지는거니 전체 list의 개수나는 t*N이다.
            if result[i]>arr[t][0]:   ### 첫번쨰 index의 값보다 큰 값이 있는 index를 저장해준다.
                Flag=True        ### 큰값을 찾았따는것을 알려주기 위해 Flag=True로 바꿔준다.
                ind=i
                break
        if Flag:    ### Flag가 True이면, 큰값의 위치가 있는 index에 하나씩 집어넣어주면 된다.
            for i in range(N-1,-1,-1):
                result.insert(ind,arr[t][i])
            t+=1          ### 그리고 다음 행으로 가주기 위해 t를 +1 해준다.
            Flag=False    ### 그리고 flag를 Flase로 초기화해준다.
        else:   
            result.extend(arr[t][:])   ### 큰값이 없는 경우엔 가장뒤에 넣어줘야하므로 extend로 이용해줬다.
            t=t+1               ### 그리고 다음 행으로 가주기 위해 t를 +1 해준다.
    print('#{} '.format(tc),end='')
    for i in range(10):
        print(result.pop(),end=' ')
    print('')
