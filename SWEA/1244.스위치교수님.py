# a, b = 1, 0
# a = a^1
# b = b^1
# print(a,b)
# arr=[0,1,2,3,4]
# print(' '.join(map(str, arr)))
import sys
sys.stdin = open('input.txt','r')
N=int(input()) #스위치
sw = [0] + list(map(int,input().split()))
M = int(input()) #학생수
for _ in range(M):
    gender, num = map(int, input().split())

    if gender == 1: #남자
        #num의 배수에 해당하는 스위치를 변경
        for i in range(num, N+1, num):
            sw[i]^=1
    else:           #여자
        sw[num] ^=1
        l, r = num-1, num+1
        while l >=1 and r <= N:
            if sw[l] != sw[r]:
                break
            sw[l] ^= 1
            sw[r] ^= 1
            l, r = l-1, r+1
sw.pop(0)
for i in range(0, len(sw), 20):
    print(' '.join(map(str, sw[i:i+20])))