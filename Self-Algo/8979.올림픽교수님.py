import sys; sys.stdin = open('input.txt','r')
N, K = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
#리스트로 각 요소 기준으로 정렬하는 법
#arr.sort(reverse=True, key=lambda x: (x[1],x[2],x[3]))

# K 번 국가의 금,은,동 수를 찾는다.
g = s = b = 0 # gold, silver, bronze
for i in range(N):
    if arr[i][0] == K:
        g,s,b = arr[i][1], arr[i][2], arr[i][3]
        break

#순위가 높은 국가의 수를 카운팅
ans=0
for i in range(N):
    if arr[i][1]>g: ans+=1
    elif arr[i][1] == g and arr[i][2] >s : ans+=1
    elif arr[i][1] == g and arr[i][2] ==s and arr[i][3]: ans+=1

print(ans+1)