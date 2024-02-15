import math
import numpy as np

x1 , y1 = map(math.radians, eval(input("첫 번째 점(위도와 경도)을 60분법 각으로 입력하세요")))
x2 , y2 = map(math.radians, eval(input("두 번째 점(위도와 경도)을 60분법 각으로 입력하세요")))

d = 6370.01 * math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))

print("두 점 사이의 거리는",d,"입니다.")