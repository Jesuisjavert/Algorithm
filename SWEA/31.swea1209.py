import sys
sys.stdin = open('input.txt','r')
for tc in range(1,11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sumlist = []
    for x in range(100):
        tmp = 0
        for y in range(100):
            tmp += arr[x][y]
        sumlist.append(tmp)
    for y in range(100):
        tmp = 0
        for x in range(100):
            tmp += arr[x][y]
        sumlist.append(tmp)
    for x in range(100):
        tmp = 0
        for y in range(100):
            if x==y:
                tmp += arr[x][y]
        sumlist.append(tmp)
    print('#{}'.format(tc),max(sumlist))
