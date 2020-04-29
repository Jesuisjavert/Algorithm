
def bine(l, r, before):
    # l : 왼쪽인덱스
    # r  : 오른쪽인덱스
    # before : 전에 선택했던 방향 (1 : 왼쪽, 2 : 오른쪽) >> 번갈아 선택했는지 검사할 거임
    m = (l+r)//2
    if(A[m]==target): return 1

    if(A[m]<target):#타겟이 중간보다 오른쪽에 위치한다구?
        l = m+1 # 오른쪽구간으로 탐색범위 수정 l인덱스값을 수정
        if(before==2):return 0 # 같은 방향을 탐색하면 조건에 어긋나기때문에 return 0
        before = 2
    else:
        r = m-1 # 왼쪽구간으로 탐색범위 수정 r인덱스값을 수정
        if(before==1):return 0
        before = 1
    return bine(l, r, before)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    ans = 0

    for i in range(M):
        target = B[i] # B에 있는 것이 A에 있는 지 확인
        if (bine(0, N-1, 0)==1): ans += 1 # A리스트에 조건에 부합하는 B리스트_target이 있으면

    print("#%d %d"%(t, ans))
