import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1, T+1):
    oven,pizza = map(int, input().split())
    cheeze = list(map(int, input().split()))
    queue = []
    for i in range(oven):
        queue.append([cheeze[i], i])
    idx = 0
    pizzaout=-1
    while len(queue)!=1:
        queue[0][0] //= 2
        if queue[0][0] == 0:
            if oven + idx < pizza:
                queue.pop(0)
                queue.append([cheeze[oven+idx], oven+idx])
                idx+=1
            elif oven+idx >= pizza:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
    print('#{} {}'.format(tc,queue[0][1]+1))