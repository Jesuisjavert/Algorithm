import sys
sys.stdin = open('input.txt','r')

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split()))for _ in range(9)]

    def lineCheck():
        for i in range(9):
            row_sum=col_sum=0
            for j in range(9):
                row_sum += arr[i][j]
                col_sum += arr[j][i]
            if row_sum != 45 or col_sum != 45: return 0

        return 1

    def rectcheck():
        for i in range(0,9,3):
            for j in range(0,9,3):
                rect = [0] * 10
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if rect[arr[x][y]]: return 0
                        rect[arr[x][y]] = 1
        return 1
        