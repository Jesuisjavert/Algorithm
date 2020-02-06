import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[int(x) for x in input().split(' ')] for y in range(N)]
    msum_result=[]
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                for t in range(M):
                    total += arr[i+k][j+t]
            msum_result.append(total)
    print('#{}'.format(test_case),max(msum_result))