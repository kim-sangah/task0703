import random

best = 1e9  # 1e9 1뒤에 0이 9개인 10억을 나타냄

while True:
    random_number = random.randint(1, 100)
    n = random_number
    count = 0

    if best != 1e9:
        print('이전 최고기록은', best, '번 입니다.')

    while True:
        x = int(input('숫자를 입력하세요: '))
        if x <= 0 or x > 100:
            print('유효한 범위 내의 숫자를 입력하세요 (1~100)')
        
        count += 1

        if x < n:
            print('업')
        elif x > n:
            print('다운')
        else:
            print('맞았습니다')
            print('시도한 횟수 : ', count)
            best = min(best, count)
            break

    while True:
        retry = input('다시하시겠습니까? (yes 또는 no)')
        if retry in ('yes', 'no'):
            break
        else:
            print('유효한 문자를 입력하세요 (yes 또는 no)')

    if retry==str('yes'):
        continue
    elif retry==str('no'):
        break

print('게임 종료! 최고기록 : ', best)
