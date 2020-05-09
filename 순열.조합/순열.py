

### length은 전체 길이, end는 내가 찾을 개수, cnt는 현재 개수
def perm(length,end,cnt):
    if cnt == end:
        print(new_arr)
    else:
        for i in range(length):
            if visited[i] == False:

                visited[i] = True
                new_arr[cnt] = i
                perm(length,end,cnt+1)
                visited[i] = False


arr = list(range(3))
N = len(arr)
k = 2
visited = [False]*N
new_arr = [-1] * k
perm(N,k,0)

