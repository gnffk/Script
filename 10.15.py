def isSorted(lst): # list 오름차순으로 정렬되어 있으면 True 변환
    # 1 2 3 4 5  -> true  항상 옆에 있는 수는 커야 한다.
    # 1 3 2 4 5 -> false
    for i in range(len(lst)-1): #i=0,1,2,......,l-2
        if lst[i] > lst[i+1]:
            return False
    return True


sList = input('정수를 입력:').split()
iList = [eval(i) for i in sList]

if isSorted(iList):
    print('정렬되어 있음')
else:
    print('정렬되어 있지 않음')