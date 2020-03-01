import sys
import itertools
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    yeonsan_cnt = list(map(int, input().split()))   #  + - * /
    yeonsan = ''
    for a in range(4):
        if a == 0:
            temp = yeonsan_cnt[a]
            while temp != 0:
                yeonsan+= '+'
                temp-=1
        elif a == 1:
            temp = yeonsan_cnt[a]
            while temp != 0:
                yeonsan+= '-'
                temp-=1
        elif a == 2:
            temp = yeonsan_cnt[a]
            while temp != 0:
                yeonsan+= '*'
                temp-=1
        elif a == 3:
            temp = yeonsan_cnt[a]
            while temp != 0:
                yeonsan+= '/'
                temp-=1
    allchance=set(itertools.permutations(yeonsan,len(yeonsan)))
    allchancelist = list(allchance)
    numbers = list(map(int, input().split()))
    allpossibleresult = []
    for p in allchancelist:
        tempnumbers = numbers[:]
        cnt = 0
        while len(tempnumbers) > 1:
            first = tempnumbers.pop(0)
            second = tempnumbers.pop(0)
            while cnt < len(allchancelist):
                if p[cnt] is '+':
                    tempnumbers.insert(0,first+second)
                    cnt+=1
                    break
                elif p[cnt] is '-':
                    tempnumbers.insert(0,first-second)
                    cnt+=1
                    break
                elif p[cnt] is '*':
                    tempnumbers.insert(0,first*second)
                    cnt+=1
                    break
                elif p[cnt] is '/':
                    if second != 0:
                        tempnumbers.insert(0,int(first/second))
                        cnt+=1
                        break
        allpossibleresult.append(*tempnumbers)
    print('#{}'.format(testcase),max(allpossibleresult)-min(allpossibleresult))