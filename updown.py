import random

count = 0

random_number = random.randint(1, 100)
n = random_number

while True:
    x = int(input("숫자를 입력하세요: "))
    count += 1

    if x <= 0 or x > 100:
        print("유효한 범위 내의 숫자를 입력하세요 (1~100)")

    else:
        if x < n:
            print("업")
        elif x > n:
            print("다운")
        if n == x:
            print("맞았습니다")
            print("시도한 횟수 : " + str(count))
            break 