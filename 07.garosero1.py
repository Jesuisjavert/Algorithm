for test_case in range(0, 10):
    T = int(input())
    N = 100
    arr = [list(map(int, input().split())) for i  in range(N)]
    MAX = 0
    eorkrtjs1 = eorkrtjs2 = 0
    garo = 0
    sero = 0
    for i in range(N):
        eorkrtjs1 += arr[i][i]
        eorkrtjs2 += arr[i][99-i]
        for j in range(N):
            garo += arr[i][j]
            sero += arr[j][i]
        MAX = max(garo, sero, eorkrtjs1, eorkrtjs2)
        print(f'{T},{Max}')