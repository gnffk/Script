def ex():
    x,y = eval(input("점의 x와 y좌표값을 입력하세요:"))

    judge(x,y)

def judge(x,y):
    g = lambda x,y : y - (x/(-2))
    if g(x,y)>=0 and g(x,y)<=100 and x >= 0  and x<=200 and y>=0 and y<=100:
        print("점은 삼각형 내부에 있습니다.")
    else:
        print("점은 삼각형 외부에 있습니다")

ex()