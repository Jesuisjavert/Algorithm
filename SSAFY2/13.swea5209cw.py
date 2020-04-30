#### ind의 위치를 저장할 list를 result , k 는 depth , end는 끝날 위치, sub_sum은 중간합
def backtrack(result,k,end,sub_sum):
    global minV
    c=[0]*N  #### make_candidate에서 쓰기 위한거 기능은 result와 동일하다.
    if k == end:  ### 끝에 도착하면 합을 비교한다.
        if minV>sub_sum:
            minV = sub_sum
            return
    else:
        if sub_sum > minV:  ### 중간에 값
            return
        ncands = make_candidate(result,k,end,c) #### 순열을 만들어주는 거 여기가 중요하다.
        for i in range(ncands):
            result[k] = c[i]   #### 그리고 make_candidate에서 만든 c의 값을 result에 넣어준다.
            backtrack(a,k+1,end,sub_sum+V[k][a[k]])  ### 그리고 난뒤 backtrack을 반복해준다.
        ##### backtrack 최초 진입 후 
        #### make_candidate를 나오면 c는 [0,1,2]이 저장되서 나온다.
        #### 두번째 backtrack부터는 처음 값에 따라 달라진다.
        #### 처음 선택값     두번째 선택값
        ####      0     ----      1
        ####            ----      2
        ##############################
        ####      1     ----      0
        ####            ----      1
        ##############################
        ####      2     ----      0
        ####                      1
        ###############################
        ### 즉 makecandidate는 중복되지않은 순열을 더 효율적으로 만들어주기 위함이다.
#### rr은 backtrack의 result와 동일 구분하기 위해서 해줬다.  cc도 backtrack의 c와 동일하다.
def make_candidate(rr,k,end,cm):
    in_perm = [False] * end  ### 먼저 N의 크기와 동일한 in_perm을 만들어준다.
    for i in range(k):#### 이건 k가 1이 되었을때부터 작동하기 위한것이다.
        in_perm[rr[i]] = True #### 우리가 result에 넣어준 index을 중복을 방지하기 위함이다. 
                              #### 최초에는 만약에 end 가 3이라면 0,1,2 즉 모든 수가 들어갈수 있으므로 작동안하도록 range(k)로 해놨다.
                              #### k가 0보다 커진경우 rr에 있는 값들을 가져와서 이미 쓴 값들은 True로 만들어준다.
    ncand = 0   ### 이건 make_candidate를 나온뒤 backtrack에서 몇번이나 돌릴지 결정해주는것이다.
    for i in range(N):
        if not in_perm[i]:  ### 만약에 탐색안된 값들이 있으면,
            cm[ncand] = i  #### 그 값들을 cm에 저장을 해준다.
            ncand +=1      #### 그리고 개수를 늘려준다.
    return ncand
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    a = [0] * N    
    minV = 1000000
    total_sum=0
    backtrack(a,0,N,0)
    print('#{} {}'.format(tc, minV))