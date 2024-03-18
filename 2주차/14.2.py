def ex():
    s = input("정수 리스트 입력: ")
    intList = [eval(i) for i in s.split()]
    d = {} # key: 정수 value : 빈도수
    for n in intList:
        if n in d: # 이미 n 정수 값이 딕셔너리에 키값으로 이미 존재
            d[n] +=1
        else:
            d[n] = 1
    maxCount = max(d.values())
    for k,v in d.items():
        if v == maxCount:
            print(k, end = " ")
    print()

ex()