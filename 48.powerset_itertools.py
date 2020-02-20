import itertools
b=list(range(1,11))
for k in range(1,11):
    t=itertools.permutations(b,k)
    for i in t:
        temp=0
        for ttt in i:
            temp+=ttt
        if temp<=10:
            print(i)