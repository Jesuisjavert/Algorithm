import sys
sys.stdin = open('input.txt','r')
T = int(input())

for tc in range(1, T + 1):
    N,M,L = list(map(int,input().split()))
    lis = list(map(int,input().split()))
    for i in range(M):      
        arr=input().split()        
        if arr[0]=='I':
            n1=int(arr[1])
            n2=int(arr[2])            
            lis.insert(n1,n2)     
        elif arr[0]=='D':
            n1=int(arr[1])
            lis.pop(n1)
        else:
            n1=int(arr[1])
            n2=int(arr[2])
            lis[n1]=n2    
    if L+1>len(lis):
        result=-1
    else:
        result=lis[L]
    print('#{} {}'.format(tc,result))