from tkinter import *

import pygame

pygame.init()
root = Tk()
root.title("The Millionaire Game")
root.geometry('1352x652+0+0')
root.configure(background='black')
#############################Frames#############################################
# main frame
ABC = Frame(root, bg='black')
ABC.grid()

# two subframes in the main frame
ABC1 = Frame(root, bg='black', bd=20, width=900, height=600)
ABC1.grid(row=0, column=0)

ABC2 = Frame(root, bg='black', bd=20, width=452, height=600)
ABC2.grid(row=0, column=1)

# all the lifelines to be there in the first frame ABC1
ABC1a = Frame(ABC1, bg='black', bd=20, width=900, padx=110, height=200)
ABC1a.grid(row=0, column=0)
ABC1b = Frame(ABC1, bg='black', bd=20, width=900, height=200)
ABC1b.grid(row=1, column=0)
ABC1c = Frame(ABC1, bg='black', bd=20, width=900, height=200)
ABC1c.grid(row=2, column=0)


###########################ImagesChange#############################################

def Change50_50():
    canvas = Canvas(ABC1a, bg='black', width=180, height=80)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file='cross_5050.png')
    canvas.create_image(90, 40, image=image1)
    canvas.image = image1


def PeopleChange():
    canvas = Canvas(ABC1a, bg='black', width=180, height=80)
    canvas.grid(row=0, column=1)
    canvas.delete("all")
    image2 = PhotoImage(file='cross_people.png')
    canvas.create_image(90, 40, image=image2)
    canvas.image = image2


def PhoneChange():
    canvas = Canvas(ABC1a, bg='black', width=180, height=80)
    canvas.grid(row=0, column=2)
    canvas.delete("all")
    image3 = PhotoImage(file='cross_phone.png')
    canvas.create_image(90, 40, image=image3)
    canvas.image = image3


def WrongAns():
    canvas = Canvas(ABC1b, bg='black', width=300, height=200)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image3 = PhotoImage(file='wrong_ans.png')
    canvas.create_image(150, 100, image=image3)
    canvas.image = image3


def MillionPicture(i):
    canvas = Canvas(ABC2, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    if i==1:
        image4 = PhotoImage(file='Picture1.png')
    if i==2:
        image4 = PhotoImage(file='Picture2.png')
    if i==3:
        image4 = PhotoImage(file='Picture3.png')
    if i==4:
        image4 = PhotoImage(file='Picture4.png')
    canvas.create_image(215, 300, image=image4)
    canvas.image = image4


###########################Questions#############################################

Ques = StringVar()  # global
Answer1 = StringVar()  # options
Answer2 = StringVar()
Answer3 = StringVar()
Answer4 = StringVar()


def Question(i):
    if i == 1:
        Ques.set("What is 3 + 324 ?")
        Answer1.set("43")
        Answer2.set("327")  # correct ans
        Answer3.set("143")
        Answer4.set("243")
    if i == 2:
        Ques.set("What is 2+3 ?")
        Answer1.set("23")   #correct ans
        Answer2.set("32")
        Answer3.set("5")
        Answer4.set("243")

    if i == 3:
        Ques.set("What is 23*2 ?")
        Answer1.set("46")   #correct ans
        Answer2.set("321")
        Answer3.set("213")
        Answer4.set("232")



def correct_ans(i):
    if i == 1:
        return 'b'
    if i == 2:
        return 'c'
    if i == 3:
        return 'a'
start=1
def call(option):
    global start
    ans=correct_ans(start)
    if ans==option:
        MillionPicture(start)
        start+=1
        Question(start)
    else:
        WrongAns()


###########################Images#############################################
CentreImage = PhotoImage(file='center.png')
Logocenter = Button(ABC1b, image=CentreImage, bg='black', width=300, height=200)
Logocenter.grid()

Image5050 = PhotoImage(file='50_50.png')
Logo5050 = Button(ABC1a, image=Image5050, bg='black', width=180, height=80, command=Change50_50)
Logo5050.grid(row=0, column=0)

ImagePeople = PhotoImage(file='People.png')
LogoPeople = Button(ABC1a, image=ImagePeople, bg='black', width=180, height=80, command=PeopleChange)
LogoPeople.grid(row=0, column=1)

ImagePhone = PhotoImage(file='Phone.png')
LogoPhone = Button(ABC1a, image=ImagePhone, bg='black', width=180, height=80, command=PhoneChange)
LogoPhone.grid(row=0, column=2)

MillionImage = PhotoImage(file='Picture0.png')
MillionImg = Button(ABC2, image=MillionImage, bg='black', width=430, height=600)
MillionImg.grid(row=0, column=0)
##############################Text,Labels#################################
Question(1)

txtQuestion = Entry(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=44, justify=CENTER,
                    textvariable=Ques)
txtQuestion.grid(row=0, column=0, columnspan=4, pady=4)

lblQuestionA = Label(ABC1c, font=('arial', 14, 'bold'), text='A :', bg='black', fg='white', bd=5, justify=CENTER)
lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)
lblQuestionB = Label(ABC1c, font=('arial', 14, 'bold'), text='B :', bg='black', fg='white', bd=5, justify=LEFT)
lblQuestionB.grid(row=1, column=2, sticky=W)
lblQuestionC = Label(ABC1c, font=('arial', 14, 'bold'), text='C :', bg='black', fg='white', bd=5, justify=LEFT)
lblQuestionC.grid(row=2, column=0, sticky=W)
lblQuestionD = Label(ABC1c, font=('arial', 14, 'bold'), text='D :', bg='black', fg='white', bd=5, justify=LEFT)
lblQuestionD.grid(row=2, column=2, sticky=W)

op1 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                      justify=CENTER, textvariable=Answer1, command=lambda:call('a'))
op1.grid(row=1, column=1, pady=4)

op2 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                      justify=CENTER, textvariable=Answer2, command=lambda:call('b'))
op2.grid(row=1, column=3, pady=4)

op3 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                      justify=CENTER, textvariable=Answer3, command=lambda:call('c'))
op3.grid(row=2, column=1, pady=4)

op4 = Button(ABC1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=17, height=2,
                      justify=CENTER, textvariable=Answer4,command=lambda:call('d'))
op4.grid(row=2, column=3, pady=4)

root.mainloop()