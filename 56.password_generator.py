import sys
import collections
sys.stdin = open('input.txt','r')
for testcase in range(1,11):
    T = int(input())
    password = collections.deque(map(int, input().split()))
    flag = True
    while flag:
        password[0] = password[0]-1
        password.rotate(-1)
        if password[-1] <= 0:
            password[-1]=0
            flag=False
            break
        password[0] = password[0]-2
        password.rotate(-1)
        if password[-1] <= 0:
            password[-1]=0
            flag=False
            break
        password[0] = password[0]-3
        password.rotate(-1)
        if password[-1] <= 0:
            password[-1]=0
            flag=False
            break
        password[0] = password[0]-4
        password.rotate(-1)
        if password[-1] <= 0:
            password[-1]=0
            flag=False
            break
        password[0] = password[0]-5
        password.rotate(-1)
        if password[-1] <= 0:
            password[-1]=0
            flag=False
            break
    print('#{}'.format(testcase),*password)