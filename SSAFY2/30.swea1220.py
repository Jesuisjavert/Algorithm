import sys
sys.stdin = open('input.txt','r')
for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(map(list,zip(*arr)))
    cnt = 0
    for x in range(N):
        tmp = 0
        for y in range(N):
            if arr2[x][y] == 1:
                tmp= arr2[x][y]
            if arr2[x][y] == 2 and tmp==1:
                cnt+=1
                tmp=0
    print('#{}'.format(tc),cnt)

# arr = [[1,2,3],[4,5,6],[7,8,9]]
# print(arr)
# arr2 = list(map(list, zip(*arr)))
# print(arr2)
