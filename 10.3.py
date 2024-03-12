s = input("1과 100사이의 정수 입력:")
items = s.split() #문자열 리스트로 변환
numbers = [eval(x) for x in items] #정수형 리스트로 변환

print(numbers)
counts = [0]*101 #[0,0,0,,,,,0] 빈도수를 세는 리스트 변수
for value in numbers:
    counts[value] +=1 #value를 인덱스로 빈도수 증가
for i in range(1,101):
    if counts[i] >0:
        print(i, "-", counts[i],"번 나타납니다.")
