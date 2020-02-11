import sys
sys.stdin= open('input.txt','r')
def turn():
    new_arr = [[0]*N for n in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-j-1][i]
    return new_arr
T= int(input())
for testcase in range(1,T+1):
    N, direction = input().split()
    N = int(N)
    arr = [[int(x) for x in input().split()] for y in range(N)]

    # temp = []
    # for x in range(N):
    #     t = []
    #     for y in range(len(arr[0])):
    #         if arr[x][y] != 0:
    #             t.append(arr[x][y])
    #     for i in range(len(t)):
    #         if t[i]==t[i+1]:
    #             t[i]=t[i-1]*2
    #             t.remove(i+1)
    #     temp.append(t)
    # print(temp)
    #
    #
    #
    #
    #
    #
    # # for i in range(N):
    # #     for j in range(len(arr[0])):
    # #         if temp[i][j]==temp[i][j+1]:
    # #             temp[i][j] = (temp[i][j])*2
    #             temp[0][1]

