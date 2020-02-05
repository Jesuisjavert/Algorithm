import sys
sys.stdin = open("input.txt", "r", encoding='UTF8')
T = int(input())
for test_case in range(1, T + 1):
    letter = str(input())
    first = [' ']
    second = [' ']
    third = ['♡']
    fourth = [' ']
    fifth = [' ']
    for let in letter:
        third.append(' {}'.format(let))
    for n in range(len(letter)):
        first.append(' ♡ ')
        second.append('♡ ♡ ')
        fourth.append('♡ ♡ ')
        fifth.append(' ♡ ')
    print(''.join(first))
    print(''.join(second))
    print(''.join(third))
    print(''.join(fourth))
    print(''.join(fifth))

