import sys
sys.stdin = open("input.txt", "r")
'''
1. 동서방향 리스트(너비), 남북방향리스트(높이), 각각의 변의 길이를 순서별로 정렬한 lengthlist 생성
2. productivity(각 1평방미터당 생산성 input값 담아줌),input값 담아줌. 
3. 큰 사각형 넓이(max너비*max너비)에서 작은사각형 넓이를 빼줄거임
4. lengthlist의 순서를 통해 작은 사각형의 가로와 세로를 찾아내는 법을 구현함.
   (작은 사각형의 높이는 자신의 앞뒤의 합이 큰 사각형의 가로와 같으면 그 변이 세로;
    가로 역시 자신의 앞뒤의 합이 큰사각형의 세로와 같으면 그 변이 가로)
5. result에 (큰 사각형 - 작은 사각형) 생산성 해줌 
'''

productivity = int(input())
eastwest = []   #너비리스트
southnorth = [] #높이리스트
lengthlist=[] #각 변의 길이를 순서대로 정렬한 리스트
for n in range(6):
    way, length= map(int, input().split())
    if way in [1,2]:
        eastwest.append(length) #동서
    if way in [3,4]:
        southnorth.append(length)   #남북
    lengthlist.append(length)
nulbi= max(eastwest)*max(southnorth)    #큰 사각형 넓이
lengthlist=lengthlist*2 #한 바퀴만 돌면 잘 못 찾는 경우가 있길래 2바퀴 돌림
garo,sero=0,0
for i in range(len(lengthlist)-2):
    if lengthlist[i] + lengthlist[i+2] == max(eastwest):
        sero = lengthlist[i+1]
    if lengthlist[i] + lengthlist[i+2] == max(southnorth):
        garo = lengthlist[i+1]  #for문으로 작은 사각형 가로세로 찾아줌
# print(garo,sero)
result = (max(eastwest)*max(southnorth))-(garo*sero)
print(result*productivity)