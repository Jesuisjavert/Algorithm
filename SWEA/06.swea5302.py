def search(dock,idx):
    end=dock[idx][1]
    while True:
        start=25
        arr=True
        for i in dock:
            if i[0]>=end:
                if start>i[1]:
                    start=i[1]
                    arr=False
        end=start
        if arr:
            break
        else:
            idx+=1
    return idx+1
T=int(input())
for tc in range(1,1+T):
    N=int(input())
    result=[]
    for i in range(N):
        arr=list(map(int,input().split()))
        result.append(arr)
    result.sort(key=lambda x : x[1])
    result=search(result,0)
    print('#{} {}'.format(tc,result))