import sys
sys.stdin = open('input.txt','r')
T = int(input())
numlist = [str(x) for x in range(1,T+1)]
for a in numlist:
    cnt = 0
    for b in range(len(a)):
        if a[b] in ['3','6','9']:
            cnt +=1
            if cnt == 3:
                numlist[int(a)-1] = '---'
            if cnt == 2:
                numlist[int(a)-1] = '--'   
            if cnt == 1:
                numlist[int(a)-1] = '-'
print(*numlist)
        
