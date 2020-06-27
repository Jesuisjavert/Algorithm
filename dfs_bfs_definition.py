def dfs(graph, start_node):
    visit = list()
    stack = list()
    stack.append(start_node)
    visit[start_node] = True
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
        return visit

                
def bfs(graph, start_node):
    visit = list()
    queue = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
        return visit

def bfs(graph, start,endlist):  #GOD호진
    visit = list()
    queue = list()
    endstack=list(endlist)
    queue.extend(start)
    while queue:
        node = queue.pop(0)
        if node not in start:
            endstack.remove(node)
        if (node not in visit) and (node not in queue) and (node not in endstack):
            visit.append(node)
            queue.extend(graph[node])


def dfs(v):
    stack = []
    stack.append(v)
    visited[v] = True
    while stack :
        v = stack.pop(-1)
        print(v, end=' ')
        for w in G(v):
            if not visited[v]:
                visited[v].append(v)
                stack.extend()
    return visited[v]
