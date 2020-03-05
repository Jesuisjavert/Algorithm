import sys
import itertools
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,3):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chance = []
    for i in range(N):
        selectone = list(itertools.permutations(arr[i],1))
        print(selectone[i])

    # chance = list(itertools.combinations(arr,1))
    # print(chance)