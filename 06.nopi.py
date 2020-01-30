import sys
sys.stdin = open("input.txt", "r")

T=10
for test_case in range(1,T+1):
    appart = int(input())
    num=[int(number) for number in input().split()]
    result = 0
    for i in range(2,int(appart)-2):
        if num[i] == max(num[i-2],num[i-1],num[i],num[i+1],num[i+2]):
            result += (num[i] - max(num[i-2],num[i-1],num[i+1],num[i+2]))
    print('#'+str(test_case), result)