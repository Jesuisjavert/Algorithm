arr = [3,6,7,1,5,4]
n = len(arr) #n은 원소의 개수
for i in range(1<<n): ##1<<n: 부분 집합의 개수
    for j in range(n+1): ##원소의 수만큼 비트를 비교함
        if i & (1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=",")
    print()
print()