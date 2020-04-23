import sys; sys.stdin = open('4839.txt','r')

def binarySearch(lo, hi, key):
    if lo> hi: return 0
    mid = (lo + hi) >> 1
    if mid == key:
        return 1
    elif mid > key:
        binarySearch(lo, mid, key) + 1
    else:
        binarySearch(lo, mid, key) + 1

for tc in range(1, int(input())+1):
    p, pa, pb = map(int, input().split())

    A = binarySearch(1, p, pa)
    B = binarySearch(1, p, pb)