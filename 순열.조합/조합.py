

## n,k , cnt는 우리가 몇번 골랐는지 해주는거, ind는 뒤에걸 탐색안해주기 위해서
def combi(N,K,cnt,ind):

    if cnt == K:
        print(new_arr)
        return
    else:
        for i in range(ind,N):  
            if visited[i] == False:
                visited[i] = True
                new_arr[cnt] = arr[i]
                combi(N,K,cnt+1,i)
                visited[i] = False

arr = list(range(10))
N = len(arr)
k = 3
new_arr = [-1] * k
visited = [False] * N

combi(N,k,0,0)
