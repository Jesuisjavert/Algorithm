import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    target = int(sum(arr)/N)
    differences = 0
    for num in arr:
        differences += abs(num - target)
    print('#{}'.format(tc),int(differences/2))