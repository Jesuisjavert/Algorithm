import sys
sys.stdin = open("input.txt", "r")
a, b = map(int, input().split())
arr = [[1]*a for _ in range(b)]
N = int(input())
garolist=[0,b]
serolist=[0,a]
for line in range(N):
    garo0sero1, line = map(int, input().split())
    if garo0sero1==0:
        garolist.append(line)
    if garo0sero1==1:
        serolist.append(line)
garolist.sort()
serolist.sort()
garolen=[]
serolen=[]
for idx,val in enumerate(garolist):
    if idx+1<len(garolist):
        garolen.append(int(garolist[idx+1]-garolist[idx]))
for idx,val in enumerate(serolist):
    if idx+1<len(serolist):
        serolen.append(int(serolist[idx+1]-serolist[idx]))
nulbi=[]
for x in garolen:
    for y in serolen:
        nulbi.append(x*y)
print(max(nulbi))