import sys
sys.stdin = open('input.txt','r')

for testcase in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for n in range(N)]
    cnt = 0

    for i in range(N):
        flag = -1
        for j in range(N):
            if arr[j][i] == 1:
                flag = 1

            if arr[j][i] == 0:
                pass

            if arr[j][i] == 2 and flag == 1:
                cnt+= 1
                flag = -1

    print('#{}'.format(testcase),cnt)

                    