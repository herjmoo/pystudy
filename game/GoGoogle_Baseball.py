class GoGoogle:
    def __init__(self):
        import random
        print('='*50)
        print("{0:^40}".format("구글 가자 야구게임"))
        print('='*50+'\n')
# 정답 숫자 만들기
        long = input("몇자리 숫자로 게임하시겠습니까?. 5자리 이하숫자를 입력해주세요")
        while int(long) >5:
            print("5자리 이하 숫자를 입력해 주세요")
            long = input("몇자리 숫자로 게임하시겠습니까?")
        print("10번안에 맞추지 못하시면 탈락입니다")
        answer = []
        while len(answer) < int(long):
            a = random.randrange(1, 10)
            if a not in answer:
                answer.append(a)
        print(answer)

        count = 0
        s = 0

        while s != int(long):
            # 정답과 비교하기
            a = 0
            s = 0
            b = 0
            o = 0

            guess = input("%s자리 숫자를 입력해주세요: " % long)
            if len(guess) != int(long):
                print("%s자리수를 입력하셔야합니다\n" % long)
                continue

            # Strike 조건
            while a < int(long):
                if answer[a] == int(guess[a]):
                    s += 1
                a += 1

            # Ball 조건
            a = 0
            while a < int(long):
                if int(guess[a]) in answer:
                    if answer[a] != int(guess[a]):
                        b += 1
                a += 1

            # Out 조건
            a = 0
            while a < int(long):
                if int(guess[a]) not in answer:
                    o += 1
                a += 1

            count += 1
            print("%d번째 시도 %d 스트라이크 %d 볼 %d 아웃 입니다.\n" % (count, s, b, o))

            if count == 10:
                print("10번째 오답입니다. 탈락하셨습니다.")
                break

        if s == int(long):
            print("정답입니다. %d번만에 맞추셨습니다" % count)
            if count == 1:
                print("천재인듯?")
#test = GoGoogle()
