import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    str1 = input()
    str2 = input()
    bool = 0
    if str1 in str2:
        bool = 1
    print('#{}'.format(testcase),bool)