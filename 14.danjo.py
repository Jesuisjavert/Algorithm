import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    gob = []
    for i in range(N):
        for j in range(i+1, N):
            gob.append(num[i]*num[j])
    choijonglist = []
    for number in gob:
        if number // 10 != 0:
            fail = 0
            choijong = number
            chueum = number % 10
            number = number // 10
            while number > 0:
                temp = number % 10
                if temp > chueum:
                    fail += 1
                number = number // 10
                chueum = temp
            if fail == 0:
                choijonglist.append(choijong)
    if len(choijonglist)==0:
            print('#{} -1'.format(test_case))
    else:
        print('#{} {}'.format(test_case,max(choijonglist)))