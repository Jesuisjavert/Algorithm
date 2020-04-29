def backtrack(a, k, input,c):
    c = [0]*N
    if k == input:
        process_solution(a,k,sum)
    else:
        if sum > minV:
            return
        k +=1
        ncands = make_candidates(a,k,input,c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input, sum+V[k][i])

def process_solution(a, k,sum):
    global minV
    for i in range(N):
        sum += V[i][a[i+1]]
    if minV > sum:
        sum = minV
    return sum

def make_candidates(a,k,input,c):
    in_perm = [False]*N

    for i in range(1, k):
        in_perm[a[i]] = True

    ncand = 0
    for i in range(N):
        if not in_perm[i]:
            c[ncand] = i
            ncand += 1
    return ncand

# def perm(k,sum):
#     global minV
#     if k == N:
#         if sum < minV:
#             minV = sum
#     else:
#         for i in range(N):
#             if not visited[i]:
#                 a[k] = i
#                 visited[i] = True
#                 perm(k+1, sum+V[k][i])
#                 visited[i] = False

import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    a = [0] * N    
    minV = 1000000
    sum=0
    # perm(0,0)
    backtrack(a,0,N,0)
    print('#{} {}'.format(tc, minV))
