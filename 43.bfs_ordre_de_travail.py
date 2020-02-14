def bfs(graph, start,endlist):
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
        ###불필요한 코드
        # if node not in visit:
        #     visit.append(node)
        #     queue.extend(graph[node])
    return visit
import sys
sys.stdin = open('input.txt','r')
for testcase in range(1,11):
    V, E = map(int, input().split())
    graph = {}
    ###딕셔너리 갯수는 1부터 노드갯수만큼만 생성하면 됨
    for i in range(0, 10000):#10000 -> V
        graph[i] = []
    graphlist = list(map(int,input().split()))
    startlist = [graphlist[i] for i in range(len(graphlist)) if i % 2 == 0]
    endlist = [graphlist[i] for i in range(len(graphlist)) if i % 2 == 1]
    for i in range(E):
        graph[startlist[i]] += [endlist[i]]
    start = []

    ### 시작점 선별하는것을 딕셔너리 키값중에서 endlist에 없는 값을 뽑으면 시작점들
    for i in startlist:###startlist-> graph
        if i not in endlist:
            if i not in start:### i를 딕셔너리에서 뽑을 경우 딕셔너리 키값은 중복불가하므로 불필요한 코드
                start.append(i)
    result = bfs(graph, start, endlist)
    # print(len(result), V, len(graph))  ### 해당줄을 실행 하면 변화를 확인 가능
    print('#{}'.format(testcase),*result)

