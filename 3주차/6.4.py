def main():
    number= eval(input("숫자 입력:"))
    print(number,"의 reverse:", reverse(number))

def reverse(number):
    result = 0
    while number:
        result = result * 10 + number % 10
        number = number // 10
    return result
main()