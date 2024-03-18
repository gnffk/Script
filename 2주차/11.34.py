def ex():
    point=[]
    s= input("6개의 점을 입력하세요")
    temp= [eval(x) for x in s.split()]
    for x in range(6):
        point.append((temp[2*x],temp[2*x+1]))

    print("최우측하단의 점은" ,getRightmostLowestpoint(point))


def getRightmostLowestpoint(p):
    max =[]
    for x in p:
        if x[1]<0:
            max.append(x)
    temp1=max[0]
    for x in max:
        if temp1[0]<x[0]:
            temp1=x

    return temp1


ex()
