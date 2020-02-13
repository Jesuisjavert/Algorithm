import sys
sys.stdin = open('input.txt','r')
T = int(input())
def dfs(graph, start_node):
    visit = list()
    stack = list()
    stack.append(start_node)
    while stack :
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

for testcase in range(1,T+1):
    V, E = map(int,input().split())
    graph = {}
    for i in range(1,V+1):
        graph[i] = []           #기본 세팅 쫙 안 깔아주면 키값 오류남
    for i in range(E):
        a,b = map(int, input().split())
        graph[a]+=[b]            #get으로도 할수는 있지만 키값이 빵꾸남
    print(graph)
    S, G = map(int,input().split())
    final_destination = dfs(graph, S)
    result = -1
    if G in final_destination:
        result = 1
    else:
        result = 0
    print('#{}'.format(testcase),result)
