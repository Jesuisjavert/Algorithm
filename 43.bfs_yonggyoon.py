import collections
def bfs():
    result = []
    q = collections.deque()
    for i in range(1, V + 1):
        if cnt[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        result.append(node)
        for n in graph[node]:
            cnt[n] -= 1
            if cnt[n] == 0:
                q.append(n)
    return ' '.join(map(str, result))
for T in range(1, 11):
    V, E = map(int, input().split())
    a = list(map(int, input().split()))
    graph = [[] for i in range(V + 1)]
    cnt = [0] * (V + 1)
    for i in range(0, E * 2, 2):
        graph[a[i]].append(a[i + 1])
        cnt[a[i + 1]] += 1
    print('#{} {}'.format(T, bfs()))