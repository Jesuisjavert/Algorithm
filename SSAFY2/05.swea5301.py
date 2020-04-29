T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    weight=list(map(int,input().split()))
    weight.sort(reverse=True)
    truck=list(map(int,input().split()))
    truck.sort(reverse=True)
    result=0
    for car in truck:
        for idx,val in enumerate(weight):
            if val<=car:
                result+=val
                del weight[idx]
                break

    print('#{} {}'.format(tc,result))

