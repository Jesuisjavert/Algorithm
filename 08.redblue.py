import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    blue_list = []
    red_list = []
    cnt = 0
    for n in range(N):
        x1, y1, x2, y2, color = (map(int, input().split()))
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if color == 1:
                    red_list.append([x,y])
                if color == 2:
                    blue_list.append([x,y])
    for red in red_list:
        if red in blue_list:
            cnt += 1
    print('#'+str(test_case), cnt)

