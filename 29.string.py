import sys
sys.stdin = open('input.txt','r')
for t in range(1, int(input()) + 1):
    tc, N = input().split()
    ls = list(input().split())
    arr = [0] * 10
    a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(10):
        arr[i] = ls.count(a[i])
    print(tc)
    for i in range(10):
        print((a[i] + ' ') * arr[i], end='')
    print()