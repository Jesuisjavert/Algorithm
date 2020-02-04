T = int(input())
for test_case in range(1, T + 1):
    N, K = (map(int, input().split()))
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    booboon = []
    print(N, K)
    n = len(arr)  # n : 원소의 개수
    for i in range(1 << n):  # 1<<n: 부분 집합의 개수
        booboo = []
    for j in range(n + 1):  # 원소의 수만큼 비트를 비교함
        if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            booboo.append(arr[j])
    if len(booboo) == N and sum(booboo) == K:
        booboon.append(booboo)
#print(booboon)
