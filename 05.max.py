import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    num = [int(number) for number in input().split(" ")]
    maxnum=0
    mininum=1000001
    for i in num:
        if i>maxnum:
            maxnum = i
        if i<mininum:
            mininum = i
    dif = maxnum - mininum
    print('#'+str(test_case),dif)