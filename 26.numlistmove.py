import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = [int(x) for x in input().split()]
    M_list = [int(x) for x in input().split()]
    res = []
    if N>M:
        for i in range(N - M + 1):
            total = 0
            for k in range(M):
                total += N_list[i+k]*M_list[k]
            res.append(total)
    else:
        for i in range(M - N + 1):
            total = 0
            for k in range(N):
                total += M_list[i+k] * N_list[k]
            res.append(total)
    print('#{}'.format(test_case),max(res))