import random
deck = [i for i in range(52)] #52장 카드 숫자 0,1,2,......51]

numbers = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suits = ['스페이드','다이아몬드','하트','클로바']
random.shuffle(deck)

for i in deck:
    quot = i // 13 # quot = 0,1,2,3
    rem = i % 13 # rem = 0,1,2,...12
    print(suits[quot], numbers[rem] )

    # 파이썬은 수 일치 문이 없기 때문에 case 인덱스로 선택이 되게 하는 방법이 있다.