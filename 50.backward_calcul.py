def plus(a,b):
    return int(a)+int(b)
def minus(a,b):
    return int(a)-int(b)
def multiple(a,b):
    return int(a)*int(b)
def divide(a,b):
    return int(a)//int(b)

import sys
sys.stdin = open('input.txt','r')
T = int(input())
for testcase in range(1,T+1):
    equation = list(map(str, input().split()))
    stack = []
    operator = ['+','-','*','/']
    for letter in equation:
        if letter.isdecimal() :
            stack.append(letter)
        if letter in operator:
            if letter == '+':
                try:
                    a = stack.pop()
                    b = stack.pop()
                    result = plus(b,a)
                    stack.append(result)
                except:
                    print('#{}'.format(testcase),'error')
                    break
            if letter == '-':
                try:
                    a = stack.pop()
                    b = stack.pop()
                    result = minus(b,a)
                    stack.append(result)
                except:
                    print('#{}'.format(testcase),'error')
                    break
            if letter == '*':
                try:
                    a = stack.pop()
                    b = stack.pop()
                    result = multiple(b,a)
                    stack.append(result)
                except:
                    print('#{}'.format(testcase),'error')
                    break
            if letter == '/':
                try:
                    a = stack.pop()
                    b = stack.pop()
                    result = divide(b,a)
                    stack.append(result)
                except:
                    print('#{}'.format(testcase),'error')
                    break
        elif letter == '.':
            if len(stack) == 1:
                print('#{}'.format(testcase),stack[0])
            else:
                print('#{}'.format(testcase),'error')
                break
            