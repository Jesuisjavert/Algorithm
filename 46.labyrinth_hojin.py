import sys
sys.stdin = open('input.txt','r')
T = 10
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(10):
    t = input()  ## 어쩌피 이 t값을 대체할수 있는 tc값이 있기때문에 이런거는 그냥 변수에 담지말고 input()으로 흘려보내기만 하는게 좋음
    # input()
    arr = [list(map(int, input())) for x in range(16)]
    L = len(arr)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  ##이렇게 테스트 케이스마다 반복해서 사용할 값들은 전역변수로 지정하는게 좋음
    startX, startX = 1, 1
    res = -1
    cross = []  ##
    while True:
        x, y = startX, startY  ###0. startx와 starty는 현재위치를 고정하는 값으로 위치이동을 하기 전까지는 수정하지 않아야하기에 좌표이동이 필요할때는 새로운 변수에 담아서 새변수를 변경
        # print('sx',startX,'sy',startY)
        # print('x',x,'y',y)
        if arr[startX][startY] == 3:  ######아래 99번 주석 참조
            res = 1
            break
        else:
            arr[startX][startY] = 5  # 1 ## 지나온길을 0에서 출발지를 의미하는 2와 도착지를 의미하는 3을 제외한 다른숫자를 해야하는데 1보다는 다른숫자로해야 시각화하기 좋음

        # 탐색과정을 확인할수 있는 코드
        for i in arr:
            print(i)
        # print('------------------------------------------------')

        zeroCnt = 0  # , cross = 0, [] # 교차점을 나타내는 cross를 여기서 선언하면 한칸움직일때마다 초기화 되어버림
        for d in range(4):
            tx, ty = startX + dx[d], startY + dy[d]  ###1. tx ty는 다음에 갈수있는 가능성을 가진 좌표일뿐 다음으로 확정된 좌표가아님
            if zeroCnt >= 1 and arr[tx][ty] in [0, 3]:  ## 99-1. 여기부터 잘보면 사실 이동할수 있는 좌표는 0뿐만 아니라 3도 이동가능함.
                ##99-3. 여기도 마찬가지== 0:             ## 그런데 코드상으로는 0일때만 확정좌표에 담아주기때문에
                ## 이동은 잘 함에도 불구하고 3을 만나지 못했다고 0을 반환함
                cross.append([startX, startY])
            elif arr[tx][ty] in [0, 3]:  # == 0:      ##99-2. 그렇기 때문에 좌표를 담아줄때는 0인값과 3인값을 둘다 담아줘야하기에 다음과같이 바꿔줘야합니다
                x, y = tx, ty  ###2. 그렇기에 다음에 갈수있는 가능성을 가진 좌표중 0인값이있으면 갈수있다는것이기 때문에 확정된좌표인 x,y에 담아줌
                zeroCnt += 1
        if zeroCnt == 0 and len(cross) == 0:
            res = 0
            break
        elif zeroCnt == 0:
            startX, startY = cross.pop()
        ## 똑같은 if 문이지만 zeroCnt==0이라는 조건이 반복되기 때문에 아래와 같은 조건문으로도 표현가능
        # if zeroCnt==0:
        #     if len(cross) == 0:
        #         res=0
        #         break
        #     else:
        #         startX, startY =cross.pop()
        else:
            # startX, startY = tx, ty ###3. 그리고 다음 시작좌표에는 확정된 값을 다시 담아줌
            startX, startY = x, y  ###4. 이렇게 써야함 ㅇㅇ
    print('#{} {}'.format(t, res))