import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    leftlist = [0]*(E+2)
    rightlist= [0]*(E+2)
    inputlist=list(map(int,input().split()))
    for idx,val in enumerate(inputlist):
        if idx%2 == 0 and 0<=idx<len(inputlist):
            if leftlist[val]!=0:
                rightlist[val]=inputlist[idx+1]
            else:
                leftlist[val]=inputlist[idx+1]
    cnt=1
    st=[]
    st.append(N)
    while st:
        x=st.pop()
        if x:
            if leftlist[x]:
                st.append(leftlist[x])
                cnt+=1
            if rightlist[x]:
                st.append(rightlist[x])
                cnt+=1
    print('#{}'.format(tc),cnt)