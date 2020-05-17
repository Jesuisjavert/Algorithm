T=int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = {i : [] for i in range(V+1)}
    for i in range(E):
        n1,n2,w = map(int,input().split())
        adj[n1].append((n2,w))
        adj[n2].append((n1,w))
    INF = float('inf')
    parent_list = [-1]*(V+1)
    key_list = [INF]*(V+1)
    key_list[0] = 0 
    mst = [False] * (V+1)
    search_list = []
    search_list.append((0,0))
    result = 0 
    cnt = 0
    while cnt <V:
        key, node = search_list.pop()
        current_min_key = INF
        current_min_node = -1
        mst[node] = True
        for next_node, next_key in adj[node]:
            if key_list[next_node] > next_key:
                parent_list[next_node] = next_node
                key_list[next_node] = next_key
        for ind in range(V+1):
            if current_min_key > key_list[ind] and not mst[ind]:
                current_min_key = key_list[ind]
                current_min_node = ind
        result += current_min_key     
        search_list.append((current_min_key,current_min_node))
        cnt+=1
    print('#{} {}'.format(tc,result))