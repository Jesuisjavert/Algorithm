import sys
import collections
sys.stdin = open('input.txt','r')
T=int(input())
for tc in range(1,T+1):
    length, N = map(int,input().split())
    queue = collections.deque(list(map(int,input().split())))
    for _ in range(N):
        queue.rotate(-1)
    print('#{}'.format(tc), queue[0])