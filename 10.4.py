sList = (input("점수를 입력하시오:")).split()

iList = [eval(i) for i in sList]

average = sum(iList) / len(iList)

count = 0
for i in iList:
    if i >= average:
        count+=1

print("평균 이상인 점수 개수:", count)
print("평균 미만인 점수 개수:", len(iList)- count)
