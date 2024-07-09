import random

def get_player():
    while True:
        player = input('가위, 바위, 보 중 하나를 선택하세요 : ')
        if player not in (['가위', '바위', '보']):
            print('유효한 입력이 아닙니다.')
        else: 
            return player
        
draw = 0
win = 0
lose = 0

while True:

    player = get_player()

    com = random.choice(['가위', '바위', '보'])

    print(f"플레이어 : {player}, 컴퓨터 : {com}")

    if player==com :
        print('무승부')
        draw += 1
    elif player!=com:
        if ((str(player)=='가위' and str(com)=='보') or
            (str(player)=='바위' and str(com)=='가위') or
            (str(player)=='보' and str(com)=='바위')):
            print('플레이어 승리')
            win += 1
    else:
        print('컴퓨터 승리')
        lose += 1

    retry = input('다시하시겠습니까? (Y/N) ').lower()
    if retry == 'y':
        continue
    elif retry == 'n':
        break

print(f"승리 : {win}, 무승부 : {draw}, 패배 : {lose}")
