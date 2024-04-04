from tkinter import *
from tkinter.filedialog import askopenfilename #fileopen 대화상자 사용가능
def openFile():
    filenameR = askopenfilename()
    filename.set(filenameR) # Set함수로 str을 사용할수는 없지만 StringVar을 썼기 때문에 가능
    pass
def show():
    f = open(filename.get())
    S = f.read() # 파일을 읽어서 하나의 문자열로 반환
    f.close()
    newS = S.lower()
    histogram = [0] * 26 # 알파벳 빈도수 [0,0,....] 초기화
    for c in newS: # 문자열에서 문자 하나씩 가져와서
        if c.isalpha(): #알파벳이냐?
            histogram[ord(c)-ord('a')] +=1 #아스키코드가 a~z가 0번에서부터 시작하도록 바뀐다.
    for i in range(26): # i = 0,1,2,....25
        if histogram[i]: # 빈도수가 0보다 크면
            text.insert(END,chr(ord('a')+i)+'-'+str(histogram[i])+'번 나타납니다.\n') # 해당하는 아스키코드의 알파벳이 나오게 된다.

    pass
window = Tk()
window.title('문자의 출현 빈도수')
frame1 = Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill = Y)
text =Text(frame1, width = 40, height=30, wrap=WORD, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)

frame2= Frame(window)
frame2.pack()
Label(frame2, text='파일 입력:').pack(side=LEFT)
filename = StringVar()
Entry(frame2,width=20,textvariable=filename).pack(side=LEFT)
Button(frame2,text='열기', command=openFile).pack(side=LEFT)
Button(frame2,text='결과보기', command=show).pack(side=LEFT)
window.mainloop()
