import math

x1,y1,x2,y2,x3,y3 = eval(input("삼각형의 세 꼭짓점을 입력하세요:"))

s1 = ((x2-x1)**2+(y2-y1)**2)**0.5
s2 = ((x3-x1)**2+(y3-y1)**2)**0.5
s3 = ((x3-x2)**2+(y3-y2)**2)**0.5

s = (s1+s2+s3)/2

area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
area = int(area*10) / 10
#round(area,1) -> 소수점 한자리 그자리로 바꾸는게 가능
#print("삼각형의 넓이는 ",format(area,".1f")," 입니다")
print('삼각형의 넓이:', area)