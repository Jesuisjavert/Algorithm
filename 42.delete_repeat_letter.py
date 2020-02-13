def repeat(letter,b):
    for i in range(len(letter)-1):
        if letter[i]==letter[i+1]:
            letter=letter[:i]+letter[i+2:]
            return letter,0
    else:
        return letter,-1
T=int(input())
for t in range(1,T+1):
    letter=input()
    b=0
    while True:
        if b==-1:
            break
        letter,b=repeat(letter,b)
    print('#{} {}'.format(t,len(letter)))