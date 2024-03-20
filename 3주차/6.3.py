def reverse(number): # 3456 -> 6543
    result = 0
    while number:
        rem = number%10
        result = result*10 + rem
        number //= 10
    return result


def isPalindrome(number):
    if number != reverse(number):
        print('대칭수가 아님')
        return True
    else:
        print('대칭수임')
        return False

def ex():
    number = eval(input("수를 입력하라"))
    isPalindrome(number)

ex()