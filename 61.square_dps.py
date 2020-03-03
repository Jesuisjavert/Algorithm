import sys
sys.stdin = open('input.txt','r')
drow = [0, 0, 1, -1]
dcol = [1, -1, 0, 0]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    result_number = 987654321
    visited = [0] * (N**2+1)
    for row in range(N):
        for col in range(N):
            for i in range(4):
                new_row = row + drow[i]
                new_col = col + dcol[i]
                if 0<= new_row <N and 0 <= new_col<N and board[new_row][new_col] - board[row][col] ==1:
                    visited[board[row][col]] = 1
    
    i = 1
    cnt = 0
    index = 1
    while i<= N**2:
        if visited[i] == 1: 
            cnt +=1
            i +=1
            continue
        else:
            if cnt > result:
                result = cnt
                result_number = index
            elif cnt == result:
                if result_number > index:
                    result_number = index
            cnt = 0
            i +=1
        
