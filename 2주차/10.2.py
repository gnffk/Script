s = input("정수 리스트 입력:")

items = s.split()
numbers = [eval(x) for x in items]

print("정수리스트 출력 : ", numbers,"\n")

print("역순 출력 : ", list(reversed(numbers)))