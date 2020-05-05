import sys
sys.stdin = open('input.txt','r')
def shuffle(n, depth, a):
    tmp = ''.join(n)
    if depth == d:
        result_list.append(int(tmp))
        return
    else:
        for i in range(a, len(n)-1):
            for j in range(i+1, len(n)):
                n[i], n[j] = n[j], n[i]
                shuffle(n, depth+1, i)
                n[i], n[j] = n[j], n[i]
 
T = int(input())
for tc in range(1, T+1):
    num, d = input().split()
    num = list(num)
    d = int(d)
    if d % 2 == 0:
        if d > len(num):
            d = len(num)
    else:
        if d > len(num):
            d = len(num)+1
    result_list = []
    shuffle(num, 0, 0)
    print('#{} {}'.format(tc, max(result_list)))