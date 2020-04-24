import sys; sys.stdin = open('4839.txt','r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # 선택 정렬
    for i in range(10): #최소값을 찾을 범위의 시작
        if i % 2 == 0 : #짝수는 큰 값순서
            idx = i
            for j in range(i+1, N):
                if arr[idx] > arr[j]: idx=j
            arr[i], arr[idx] = arr[idx], arr[i]            
        else:
            idx= i
            for j in range(i+1, N):
                if arr[idx] > arr[j]: idx=j
            arr[i], arr[idx] = arr[idx], arr[i]