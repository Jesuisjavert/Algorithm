def turn():
    new_arr = [[0]*N for n in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-j-1][i]
    return new_arr
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for a in range(N)]
    arr = turn()
    arr1 = arr
    arr = turn()
    arr2 = arr
    arr = turn()
    arr3 = arr
    print('#{}'.format(testcase))
    for i in range(N):
        print('{} {} {}'.format(''.join(arr1[i]),''.join(arr2[i]),''.join(arr3[i])))
