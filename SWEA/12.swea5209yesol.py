
def dfs(idx, pay):
    # idx는 행(제품)index
    # pay는 생산비용

    # 현재 제품(행)에서 제품 생산할 공장(열)pick
    global ans
    global chk
    if(ans<=pay): return # 가지치기, 최소비용ans보다 현재 고르고있는 생산비용이 더 크면 더이상 진행할 필요가 없다(어차피 답이 안되기때문에) 따라서 return
    if(idx==N): # 다골랐다
        if(ans>pay):
            ans = pay # 최소비용이라면 ans갱신
            return  #더 가면 안되니까 return

    for i in range(0, N):
        if(chk[i]==0): # 현재 공장을 pick할 수 있다면
            chk[i] = 1 # 현재 공장은 pick했다 표시
            dfs(idx+1, pay+arr[idx][i])
            chk[i] = 0 # 다른 공장을 pick해줄거니까 재귀호출이 끝나고 돌아오면서 현재 공장 chk해제


T = int(input())
for t in range(1,T+1):
    ans = 123456789 # 최소비용을 구하기 위해 최대값으로 초기화
    # 한 공장당(열) 한가지 제품(행)을 골라야 하므로 뽑은 열은 다시 고르지x.
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] #이차원배열선언
    chk = [0 for _ in range(N)] # 열을 사용했는 지 체크할 chk배열

    dfs(0,0)

    print("#%d %d"%(t, ans))