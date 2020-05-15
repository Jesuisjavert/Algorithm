import sys
sys.stdin = open('input.txt','r')
for tc in range(1, 11):
    T = int(input())
    arr=[list(map(int, input().split())) for i in range(100)]
    MIN = 100000
    for x in range(100):
        if arr[0][x] == 1:
            startx = x
            cnt = 0
        for y in range(100):
            if startx != 0 and arr[y][startx-1] == 1:
                while startx != 0 and arr[y][startx-1] == 1:
                    startx -= 1
                    cnt +=1
            elif startx < 99 and arr[y][startx+1] == 1:
                while startx != 99 and arr[y][startx+1] == 1:
                    startx += 1
                    cnt +=1
        if cnt <= MIN:
            res = x
            MIN = cnt
    print('#{} {}'.format(tc, res))
