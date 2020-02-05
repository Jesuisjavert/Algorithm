N=100
maxl = 0
maxlist = []
for i in range(N):
    result = [N, i]
    j = 0
    while True:
        a = result[j] - result[j+1]
        if a < 0:
            break
        result.append(a)
        if maxl < len(result):
            maxl = len(result)
            maxlist = result[:]
        j += 1
print(maxl)
for a in maxlist:
    print(a,end=" ")
