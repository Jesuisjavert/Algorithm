def binary(left, right, before):
    m = (left+right)//2
    if A[m]==find:
        return 1
    if(A[m]<find):
        left = m+1 
        if before==2 :
            return 
        before = 2
    else:
        right = m-1 
        if before==1:
            return 0
        before = 1
    return binary(left, right, before)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(M):
        find = B[i]
        if binary(0, N-1, 0)==1:
            cnt += 1
    print('#{} {}'.format(tc, cnt))