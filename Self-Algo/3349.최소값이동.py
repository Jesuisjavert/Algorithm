import sys; sys.stdin = open('3349.txt','r')

for tc in range(1, int(input())+1):
    W, H, N = map(int, input().split())
    x, y = map(int, input().split())

    ans = 0
    for _ in range(N-1): # N-1개의 좌표를 입력
        tx, ty = map(int, input().split())
        a = x - tx
        b = y - ty
        if a * b <0:
            ans += abs(a) + abs(b)
        else:
            ans += max(abs(x-tx), abs(y-ty))

        x, y = tx, ty