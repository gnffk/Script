def m(i):

    if i == 1:
        return 1/2
    else:
        return m(i-1) + i/(i+1)

for i in range(1,21):
    print(i,'\t',m(i))
