import sys
sys.stdin = open("input.txt", "r")
T, answercountry =map(int,input().split())
medallist=[]
inputlist=[]
find=0
for n in range(T):
    a,b,c,d=map(str,input().split())
    inputlist.append(a+b+c+d)
    medallist.append(int(b+c+d))
    if int(a)==answercountry:
        find=int(b+c+d)
print(inputlist,medallist,answercountry,find)
medallist.sort(reverse=True)
print(medallist)
cnt=0
for I in range(T):
    if find==medallist[I]:
        cnt=I
        break
print(cnt+1)