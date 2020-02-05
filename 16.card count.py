import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    S= [0]*13
    D= [0]*13
    H= [0]*13
    C= [0]*13
    card = input()
    for idx, letter in enumerate(card):
        if idx % 3 == 0:
            if letter == 'S':
                S[int(card[idx+1:idx+3])-1] += 1
            elif letter == 'D':
                D[int(card[idx+1:idx+3])-1] += 1
            elif letter == 'H':
                H[int(card[idx+1:idx+3])-1] += 1
            elif letter == 'C':
                C[int(card[idx+1:idx+3])-1] += 1
    soo_list = [13-sum(S),13-sum(D),13-sum(H),13-sum(C)]
    result = []
    if 2 in [*S, *D, *H, *C] :
        result = 'ERROR'
    else:
        result = ' '.join(map(str, soo_list))
    print('#{}'.format(test_case),result)