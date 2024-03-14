import random

ball_num =eval(input("덜어뜨릴 공의 개수를 입력하세요:"))
ball_slot = eval(input("콩 기계의 슬롯 개수를 입력하세요:"))

slot = [0]*ball_slot # 0으로 초기화
for i in range(ball_num): # 공의 개수만큼 반복
    count =0
    for t in range(ball_slot-1): # 슬롯의 개수 -1만큼 반복
        if random.random() > 0.5:
            print('R', end ='') # 강제로 한줄 띄지 않도
            count +=1 # R의 개수를 센다.
        #list[t] =random.choice(['L', 'R'])
        else:
            print('L', end = '')
    print() # 한줄 띈다.
    slot[count] +=1 # 해당 슬롯의 개수를 1 증가
print(slot)

Max  = max(slot) # 최댓값
for h in range(Max, 0, -1): # h=M, M-1, M-2, ..., 1
    for s in slot:
        if s >= h:
            print('0', end = '')
        else:
            print('-', end = '')
    print('\t')