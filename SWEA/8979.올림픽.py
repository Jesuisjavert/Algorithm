N, K = map(int, input().split())

arr = [[0]*4 for _ in range(N+1)]
medal = []
for i in range(1, N+1):
    arr[i] = list(map(int, input().split()))
    if arr[i][0] == K:
        medal = arr[i]

result = 1
for i in range(1, 1+N):
    if arr[i][0] == K:
        continue
    if arr[i][1] > medal[1]:
        result += 1
    elif arr[i][1] == medal[1]:
        if arr[i][2] > medal[2]:
            result += 1
        elif arr[i][2] == medal[2]:
            if arr[i][3] > medal[3]:
                result += 1
print(result)