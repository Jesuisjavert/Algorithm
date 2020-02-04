import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    info = list(map(int, input().split()))
    upward = sorted(info)
    downward = sorted(info,reverse=True)
    result = []
    for i in range(len(upward)//2):
        result.append(downward[i])
        result.append(upward[i])
    print('#'+str(test_case),*result[0:10])
