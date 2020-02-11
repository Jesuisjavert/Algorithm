def turn():
    new_arr = [[0]*N for n in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-j-1][i]
    return new_arr
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    palinlist = []
    for n in range(N):
        for m in range(N-M+1):
            word = arr[n][m:m+M]
            reverse_word = reversed(word)
            if word == ''.join(reverse_word):
                palinlist.append(word)
    arr = turn()
    seroarr = arr
    for n in range(N):
        for m in range(N-M+1):
            word = seroarr[n][m:m+M]
            reverse_word = reversed(word)
            if ''.join(word) == ''.join(reverse_word):
                palinlist.append(''.join(word))
    print('#{}'.format(testcase),palinlist[0])