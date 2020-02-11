import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    letter = list(map(str, input()))
    letters = list(map(str, input()))
    lettersdict = {}
    for let in letters:
        lettersdict[let] = lettersdict.get(let, 0) +1
    resultdict = []
    for let in lettersdict.keys():
        if let in letter:
            resultdict.append(lettersdict[let])
    print('#{}'.format(testcase),max(resultdict))