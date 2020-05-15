# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용

# 시작점 맨왼쪽위, 도착지 가장오른쪽 아래
# 현재위치를 기준으로 상하좌우인접지역이동가능, 이동할때 기본연료 1들고 낮은지역->높은지역으로 가면 높이차만큼 추가연료
# 최소 연료 소비량구해라
# 지형이 N*N이차원배열인데 재귀dfs는 깊이가 1000이상되버리면 길을 잃어버림 (문제 N<=100, 100*100)
# 따라서 N이 크면 안전하게 큐사용 권장.
# 다익스트라방식으로 각 위치마다 최소거리를 구해줄거임

from collections import deque

def safe(y, x):
    if(0<=y and y<N and 0<=x and x<N): return 1
    return 0

INF = float('inf') # 무한대표현
dy = [0,0,1,-1]
dx = [1, -1, 0,0]
T = int(input())
for t in range(1, T+1):
    N = int(input()) # 지형정보
    arr = [list(map(int, input().split())) for _ in range(N)]  # 이차원배열선언 및 입력
    D = [[INF for _ in range(N)] for _ in range(N)] # 해당 위치로 가는 최소 distance를 담을 이차원 배열 / 최소값을 뽑아줄 거니까 최대값으로 갱신해준다.

    q = deque() # 큐 선언
    D[0][0] = 0 # 시작점에서 시작점으로 가는 비용은 0이다. / 초기화
    q.append((0,0,0 )) # q의 인자 : y, x, cost. y, x는 지형상의 현재 좌표를 나타낸다. / 큐에 시작점, 비용 푸시

    # 자 가볼까~~
    while(q):
        # 현재 y, x, cost
        y, x, cost = q.popleft()  # 큐의 맨앞 요소 삭제

        # 현재위치에서 상, 하, 좌, 우 를 탐색할거임 위로 가서 dy, dx 선언해주자.
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i] # ty, tx는 다음 갈곳의 위치(현재에서 인접한 위치)
            t_cost = cost + 1 # ty, tx 위치로 가는데 드는 비용 (기본비용+1)

            # 탐색할땐 항상 범위넘어가지 않는 지 체크,
            if(safe(ty, tx)):
                if (arr[y][x] < arr[ty][tx]):
                    t_cost += (arr[ty][tx] - arr[y][x]) # 가려는 곳이 높이가 더 높으면 높이차 만큼 추가비용발생

                if(D[ty][tx]>t_cost):
                    D[ty][tx] = t_cost
                    q.append((ty, tx, t_cost))

    print("#%d %d"%(t, D[N-1][N-1]))


