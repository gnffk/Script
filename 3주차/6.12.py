def printChars(ch1, ch2, numberPerLine):
    count = 0
    for i in range(ord(ch1), ord(ch2)+1):
        print(chr(i), end = " ")
        count +=1
        if count % numberPerLine ==0:
            print("\n")
printChars('1','Z', 10)