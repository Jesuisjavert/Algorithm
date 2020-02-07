for test in range(1,int(input())+1):
    n=int(input())
    nums=list(map(int,input().strip().split()))
    h=[]
    t=[]
    f_index=-1
    t_index=-1
    result=[]
    for i in range(2*n):
        if i%2:
            t.append(nums[i])
        else:
            h.append(nums[i])
    for i in range(n):
        if h[i] not in t:
            f_index=i
            result.append(h[i])
            result.append(t[i])
    i = 0
    while len(result)<2*n:
        for i in range(n):
            if result[~0] == h[i]:
                result.append(h[i])
                result.append(t[i])
    resultstr=' '.join(map(str,result))
    print('#{} {}'.format(test, resultstr))