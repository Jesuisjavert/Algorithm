def bfs(start):
    global result
    visited = [0] * (V+1)
    distance = [0] * (V+1)
    queue = []
    result=0
    queue.append(start)
    visited[start] = 1
    while queue:
        start = queue.pop(0)
        for next_node in range(1, V+1):
            if arr[start][next_node] and not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = 1
                distance[next_node] = distance[start] +1
                if next_node == end:
                    result = distance[next_node]
                    return
    return
T = int(input())
for tc in range(1, T+1):
    V,E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1
        arr[end][start] = 1
    start, end = map(int, input().split())
    bfs(start)
    print('#{} {}'.format(tc, result))