T=int(input())


for tc in range(1,T+1):
    N,M=map(int,input().split())

    weight=list(map(int,input().split()))
    weight.sort(reverse=True)
    truck=list(map(int,input().split()))
    truck.sort(reverse=True)
    result=0
    for tr in truck:
        for ind,we in enumerate(weight):
            if we<=tr:
                result+=we
                del weight[ind]
                break

    print('#{} {}'.format(tc,result))

