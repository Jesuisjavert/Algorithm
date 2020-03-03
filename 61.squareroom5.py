def wall(x, y):
    if x >= N or y >= N or x < 0 or y <0 or (arr[y][x] - arr[y-dy[d%4]][x-dx[d%4]] != 1):
        return False
    return True
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
     
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
 
    result_idx = 10000
    result_cnt = 0
    temp = []
     
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            testx = i
            testy = j
            cnt = 1
            temp_cnt = 0
            d = 0
            while temp_cnt < 4:
                if wall(testx + dx[d%4], testy + dy[d%4]):
                    cnt += 1
                    temp_cnt = 0
                    testx += dx[d%4]
                    testy += dy[d%4]
                else: 
                    temp_cnt += 1
                d += 1
 
            if cnt > result_cnt:
                result_cnt = cnt
                result_idx = arr[j][i]
            if cnt == result_cnt:
                result_idx = min(result_idx, arr[j][i])
             
    print('#{} {} {}'.format(t, result_idx, result_cnt))