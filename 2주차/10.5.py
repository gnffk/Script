s = input("10개의 숫자를 입력하세요:")
items = s.split()
numbers = [eval(x)for x in items]
list2 = []
for number in numbers:
    if not number in list2:
        list2.append(number)

print("중복을 제거한 고유한 숫자", list2)
