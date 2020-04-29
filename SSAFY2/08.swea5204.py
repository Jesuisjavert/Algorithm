import sys
sys.stdin = open('input.txt','r')

def merge_sort(a):
    global cnt
    if len(a) == 1:
        return a
    else:
        m=len(a) //2
        left = a[:m]
        right = a[m:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(a, left, right)
        
def merge(a, left, right):
    global cnt
    idxl=0
    idxr=0
    i = 0
    while idxl < len(left) and idxr < len(right):
        if left[idxl] < right[idxr]:
            a[i] = left[idxl]
            idxl +=1
        else:
            a[i] = right[idxr]
            idxr += 1
        i += 1
    if left[-1] > right[-1]: #5204
        cnt += 1
    if idxl < len(left):
        a[i:] = left[idxl:]
    if idxr < len(right):
        a[i:] = right[idxr:]
    return a

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    
