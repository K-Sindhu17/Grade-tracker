import tkinter
from tkinter import *

root = Tk()
root.title("Grade Tracker")
root.geometry("500x450")


def Calculations():
    english = int(englishMarks.get())
    maths = int(mathsMarks.get())
    hindi = int(hindiMarks.get())
    social = int(socialMarks.get())
    science = int(scienceMarks.get())

    # calculating total marks
    TotalMarks = (english + maths + hindi + social + science)
    Label(text = f"{TotalMarks}", font="arial 15 bold").place(x = 250, y = 220)

    # calculating average marks
    avaregeMarks = int(TotalMarks/5)
    Label(text = f"{avaregeMarks}", font="arial 15 bold").place(x = 250, y = 260)

    #display grade

    if avaregeMarks > 35:
        grade = "PASS"
    else:
        grade = "FAIL"

    Label(text = f"{grade}", font="arial 15 bold", fg="blue").place(x = 250, y = 300)


#subjects

sub_1 = Label(root, text = "English: ", font="arial 10")
sub_2 = Label(root, text = "Maths: ", font="arial 10")
sub_3 = Label(root, text = "Hindi: ", font="arial 10")
sub_4 = Label(root, text = "Social: ", font="arial 10")
sub_5 = Label(root, text = "Science: ", font="arial 10")

total = Label(root, text = "Total: ", font="arial 10")
avg = Label(root, text = "Average: ", font="arial 10")
grade = Label(root, text = "Grade: ", font="arial 10")


sub_1.place(x = 50, y = 20)
sub_2.place(x = 50, y = 60)
sub_3.place(x = 50, y = 100)
sub_4.place(x = 50, y = 140)
sub_5.place(x = 50, y = 180)


total.place(x = 50, y = 220)
avg.place(x = 50, y = 260)
grade.place(x = 50, y = 300)


englishMarks = StringVar()
mathsMarks = StringVar()
hindiMarks = StringVar()
socialMarks =StringVar()
scienceMarks = StringVar()

englishMarks = Entry(root, textvariable = englishMarks, font="arial", width=15)
mathsMarks = Entry(root, textvariable = mathsMarks, font="arial", width=15)
hindiMarks = Entry(root, textvariable = hindiMarks, font="arial", width=15)
socialMarks = Entry(root, textvariable = socialMarks, font="arial", width=15)
scienceMarks = Entry(root, textvariable = scienceMarks, font="arial", width=15)

englishMarks.place(x = 250, y = 20)
mathsMarks.place(x = 250, y= 60)
hindiMarks.place(x=250, y = 100)
socialMarks.place(x=250, y = 140)
scienceMarks.place(x=250, y = 180)

Button(text="Go", font="arial 15", bg="white", bd=10, command=Calculations).place(x=50,y=350)
Button(text="Exit", font="arial 15", bg="white", bd=10, width=8, command=lambda:exit()).place(x=350,y=350)


root.mainloop()
