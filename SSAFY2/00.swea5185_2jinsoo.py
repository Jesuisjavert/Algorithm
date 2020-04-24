import sys
sys.stdin = open('input.txt','r')
T=int(input())
for tc in range(1,T+1):
    Length,Base=input().split()
    result=''
    for letter in Base:
        sibjinsoo=int(letter,16)
        twojinsoo=format(sibjinsoo,'b')
        if len(twojinsoo)<4:
            for i in range(4-len(twojinsoo)):
                result+='0'
            result+=twojinsoo
        else:
            result+=twojinsoo
    print('#{}'.format(tc),result)