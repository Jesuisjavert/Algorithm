# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리
# 프림알고리즘사용, heapq(min heap)사용으로 최소값을 뽑을때 시간복잡도를 줄인다.

# 문제조건
# 0번부터 V번노드까지 있을 때, 최소신장트리구하기
# 프림의 동작원리를 생각하며 그대로 구현해주면 된다.

import heapq
INF = float('inf') # 무한대표현
T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())  # 노드(정점), 간선 개수
    G = list([] for _ in range(N + 1)) # 그래프구현, 리스트안에 리스트를 넣어줌
    node = [INF]*(N+1) # 노드에 최대값을 담아주고 최소값으로 갱신해줄 배열
    v = [0]*(N+1) # 노드 방문 visited배열
    pq = []
    ans = 0

    heapq.heappush(pq, (0, 0)) # heapq에 푸시 가중치, 정점 / heapq는 첫번째인자값을 기준으로 최소를 뽑음
    node[0] = 0 # 0번정점에서 0번정점까지 드는 가중치는 없으니 0으로 초기화, 프림은 아무정점이나 시작정점으로 택하면 된다.
    for i in range(E):
        # 간선의 개수만큼 입력을 받으며 가중치있는 그래프생성해준다
        F, T, cost = map(int, input().split()) # from, to, cost
        G[F].append((T, cost))
        G[T].append((F, cost))

    while(pq):
        cost, vertax = heapq.heappop(pq) # 비용(가중치),현재 정점 / 선택한정점, 선택하지 않은 정점을 연결하는 간선중에 최소값을 뽑는다다.

        if(v[vertax]): continue # 이미 방문한 정점이면 컨티뉴
        v[vertax] = 1
        ans+=cost # 가중치를 더해준다.

        # 현재 정점을 기준으로, 연결된 간선의 가중치와 node[]값 중 더 작은값으로 node값을 갱신해준다
        for i in range(len(G[vertax])):
            # 현재정점을 기준으로 연결된 정점들 for로 탐색
            t_vertax, t_cost = G[vertax][i] # 연결된 정점, 연결된 정점의 가중치
            if v[t_vertax]==0 and node[t_vertax]>t_cost :
                node[t_vertax] = t_cost # 원래 저장되있던 값보다 t_cost가 작으면 node(최소값담는배열)갱신
                heapq.heappush(pq, (t_cost, t_vertax))


    print("#%d %d"%(t, ans))