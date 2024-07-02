import random

random_rps = random.choice(["가위", "바위", "보"])
s = random_rps

x = input("가위, 바위, 보 중 하나를 선택하세요 :")

if x not in (["가위", "바위", "보"]):
    print("유효한 입력이 아닙니다.")

else:
    print("플레이어 : " + str(x) + ", 컴퓨터 : " + str(s))
    if x==s :
        print("무승부")
    elif x!=s:
        if str(x)=="가위" and str(s)=="보":
            print("플레이어 승리")
        if str(x)=="바위" and str(s)=="가위":
            print("플레이어 승리")
        if str(x)=="보" and str(s)=="바위":
            print("플레이어 승리")
        else:
            print("컴퓨터 승리")
