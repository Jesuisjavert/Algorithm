def switch(num):
    global arr
    if arr[num]==1:
        arr[num]=0
    elif arr[num]==0:
        arr[num]=1
import sys
sys.stdin = open('input.txt','r')
Switch = int(input())
arr=list(map(int,input().split()))
# print(arr)
N = int(input())
# print(N)
for tc in range(N):
    gender, touch = map(int,input().split())
    if gender == 1:
        for idx, val in enumerate(arr):
            if 0<=idx-1<len(arr) and (idx%touch)==0:
                switch(idx-1)
        # print(arr)
    else:
        touch-=1
        switch(touch)
        flag = True
        pond=1
        while flag:
            if 0<=touch-pond and touch+pond<len(arr):
                if arr[touch-pond] == arr[touch+pond]:
                    switch(touch-pond)
                    switch(touch+pond)
                    pond+=1
                if arr[touch-pond] != arr[touch+pond]:
                    flag=False
                    break
            else:
                break      
for i in range(0, len(arr), 20):
    print(' '.join(map(str, arr[i:i+20])))