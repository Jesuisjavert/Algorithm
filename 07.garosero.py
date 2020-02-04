for test_case in range(0, 10):
    T = int(input())
    N = 100
    arr = [list(map(int, input().split())) for i  in range(N)]
    MAX = 0
    eorkrtjs1 = eorkrtjs2 = 0
    garo_list=[]
    sero_list=[]
    for i in range(N):
        sero = 0
        garo = 0
        eorkrtjs1 += arr[i][i]
        eorkrtjs2 += arr[i][99-i]
        for j in range(N):
            garo += arr[i][j]
            sero += arr[j][i]
        garo_list.append(garo)
        sero_list.append(sero)
    MAX = max(max(garo_list), max(sero_list), eorkrtjs1, eorkrtjs2)
    print(MAX)