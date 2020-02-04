import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    info = list(map(int, input().split()))
    result = []
    for j in range(2):
        left = 1
        right = info[0]
        page = info[j+1]
        cnt = 0
        while left <= right:
            mid = (left+right)//2
            if mid == page:
                break
            elif mid < page:
                left = mid
                cnt += 1
            else:
                right = mid
                cnt += 1
        result.append(cnt)
    if result[0] < result[1]:
        print('#'+str(test_case),'A')
    if result[0] > result[1]:
        print('#'+str(test_case),'B')
    if result[0] == result[1]:
        print('#'+str(test_case),'0')