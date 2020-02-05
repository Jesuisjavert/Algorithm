N = int(input())
max_l = 0
max_list = []
for i in range(N+1):
    result = [N, i]
    j = 0
    while(True):
        a = result[j] - result[j+1]
        if a <= -1:
            break
        result.append(a)
        if max_l < len(result):
            max_l = len(result)
            max_list = result[:]
        j += 1
print(max_l)
for e in max_list:
    print(e, end=" ")
print()