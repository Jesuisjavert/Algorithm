import sys
import itertools
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    binary = list(input())
    tri = list(input())
    print(binary, tri)
    binum = list(itertools.permutations(binary,len(binary)))
    
    
    bipossible_nums = []
    for i in binum:
        temp = ''
        for a in range(4):
            temp += str(i[a])
        bipossible_nums.append(temp)
    print(bipossible_nums)