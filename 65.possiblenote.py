import sys
import itertools
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    note = list(map(int, input().split()))
    possible=[]
    for i in range(len(note)+1):
        chance = set(itertools.combinations(note,i))
        possible.append(chance)
    sum=0
    for a in possible:
        for b in len(possible[a]):
            print(b)
