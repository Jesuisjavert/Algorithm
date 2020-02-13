import sys
sys.stdin = open('input.txt','r')
T = int(input())
def square(n):
    if n == 1:
        return 1
    elif n ==2:
        return 3
    elif n == 3:
        return 5
    elif n >3:
        result = square(n - 1) + square(n - 2) * 2
        return result
for testcase in range(1, T + 1):
    N = int(input())
    n = int(N/10)
    res = square(n)
    print('#{}'.format(testcase),res)