import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    words = input()
    result = []
    for idx in range(len(words)):
        if words[:idx] == words[idx:idx*2]:
            result.append(words[:idx])
    print('#{}'.format(testcase),len(result[1]))
    