import sys
sys.stdin = open("input.txt", "r")
def shap(x, y):
    return sum(range(x + y)) - y + 1
def and7(n):
    a = 2
    while True:
        if n <= sum(range(a)):
            x = a - 1 - sum(range(a)) + n
            y = a - x
            break
        a += 1
    return x, y
T = int(input())
for t in range(T):
    p, q = map(int, input().split())
    x1, y1 = and7(p)
    x2, y2 = and7(q)
    result = shap(x1 + x2, y1 + y2)
    print('#{} {}'.format(t + 1, result))