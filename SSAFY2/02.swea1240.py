import sys
sys.stdin = open('input.txt','r')

T=int(input())
total=[
'0001101', #0
'0011001', #1
'0010011', #2
'0111101', #3
'0100011', #4
'0110001', #5
'0101111', #6
'0111011', #7
'0110111', #8
'0001011',]
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(input()) for _ in range(N)]
    result=[0]*8
    flag=False
    for i in range(N):
        j=M
        ind=7
        while j>7:
            a=''.join(arr[i][j-7:j])
            if a in total:
                result[ind]=total.index(a)
                ind-=1
                j-=7
                flag=True
            else:
                j-=1
        if flag:
            break
    final_result=0
    
    for i in range(8):
        if i==7:
            final_result+=result[i]
        elif i%2==0:
            final_result+=3*result[i]
        else:
            final_result+=result[i]
    if final_result%10==0:
        print('#{} {}'.format(tc,sum(result)))
    else:
        print('#{} 0'.format(tc))