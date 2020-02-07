import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    arr = [[int(x) for x in input().split()] for y in range(9)]
    garobool = 0
    for i in range(9):
        garo = 0
        for j in range(9):
            garo += arr[i-1][j-1]
            if garo == 45:
                garobool += 1
    if garobool == 9:
        garobool = True
    serobool = 0
    for p in range(9):
        sero = 0
        for q in range(9):
            sero += arr[q-1][p-1]
            if sero == 45:
                serobool += 1
    if serobool == 9:
        serobool = True
    sumbool = 0
    total = 0
    for k in range(0,9,3):
        for t in range(0,9,3):
            total = arr[k][t] + arr[k][t+1] + arr[k][t+2] + arr[k+1][t] + arr[k+1][t+1] + arr[k+1][t+2] + arr[k+2][t] + arr[k+2][t+1] +arr[k+2][t+2]
            if total == 45:
                sumbool += 1
    if sumbool != 9:
        sumbool = False
    else:
        sumbool = True
    printgab = 0
    if garobool == True and serobool == True and sumbool== True:
        printgab = 1
    else:
        printgab = 0
    print('#{}'.format(test_case),printgab)