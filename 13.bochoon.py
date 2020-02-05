N = int(input())
cnt = 0
tmp = N
while True:
    ap = tmp//10
    dwi = tmp%10
    tmp = (ap+dwi)%10 + 10*dwi
    cnt += 1
    if N == tmp:
        break
print(cnt)

n = int(input())
a = n // 10
b = n % 10
c = (a+b)%10
d = b * 10 + c
cnt = 1
Flag = True
while Flag or n != d:
    Flag = False
    a = d//10
    b = d%10
    c = (a+b)%10
    d = b*10 + c
    cnt += 1
print(cnt)