import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    arr = [[str(x) for x in input()] for y in range(5)]
    result =[]
    lenlist = []
    for i in range(len(arr)):
        lenlist.append(len(arr[i]))
    maxlength = int(max(lenlist))
    for i in range(len(arr)):
        while len(arr[i]) != maxlength:
            arr[i].append('')
    for i in range(maxlength):
         for j in range(len(arr)):
             result.append(arr[j][i])
    print('#{}'.format(test_case),''.join(result))