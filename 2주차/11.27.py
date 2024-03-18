#def sortColumns(m):
#    m.sort()
#    for i in range(len(m)):
#        if i % 3 == 0 and i != 0:
#            print()
#        print(m[i], end=" ")

def sortColumns(m):
    a = []
    for j in range(3):
        column = [m[i][j] for i in range(3)]
        column.sort()
        for i in range(3):
            m[i][j] = column[i]


def main():
    print("3X3행렬의 행 원소 입력:")
    m = []
    for i in range(3):
        s = input()
        l = [eval(i) for i in s.split()]
        m.append(l)
    sortColumns(m)
    for j in range(3):
        for i in range(3):  # 정렬된 열 출력
            print(m[j][i], end=" ")
        print()


main()