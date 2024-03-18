def sortColumns(m):
    m.sort()
    for i in range(len(m)):
        if i % 3 == 0 and i != 0:
            print()
        print(m[i], end=" ")

def main():
    print("3x3 행렬 하나씩 입력하시오: ")
    m = []
    for i in range(3):
        l = input().split()
        m.extend(l)
    sortColumns(m)


main()