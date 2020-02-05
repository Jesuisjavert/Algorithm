import sys
sys.stdin = open("input.txt", "r")
T= int(input())
for t in range(1,T+1):
    pascal=[]
    N=int(input())
    for i in range(N):
        result=[]
        if i==0:
            result=[1]
        elif i==1:
            result=[1,1]
        else:
            for j in range(i):
                if j==0:
                    result.append(1)
                else:
                    result.append(pascal[i-1][j-1]+pascal[i-1][j] )
            else:
                result.append(1)
        pascal.append(result)
    print('#{}'.format(t))
    for char in pascal:
        print(' '.join(map(str,char)))