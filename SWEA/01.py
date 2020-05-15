import sys
sys.stdin = open('input.txt','r')
T=int(input())

def Bprint(val):
    for i in range(4):
        if val&(8>>i):
            print('1', end='')
        else:
            print('0', end='')

for tc in range(1,T+1):
    N, S = input().split()

    for i in range(0, int(N)):
        t = int(S[i],16)
        Bprint(t)
        # Bprint(int(S[i]))
    print('#{}'.format(tc))