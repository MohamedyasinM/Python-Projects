import tkinter
from tkinter import END,Tk

screen = tkinter.Tk()
screen.title("Mile to kilometer Converter")
screen.minsize(height=500,width=650)


text_box1 = tkinter.Entry(width=20)
text_box1.place(x=200,y=100)

text_box2 = tkinter.Entry(width=20)
text_box2.place(x=200,y=150)

miles = tkinter.Label(text="Miles")
miles.place(x=330,y=100)

km = tkinter.Label(text="Km")
km.place(x=330,y=150)

is_equal_to = tkinter.Label(text="is Equal to")
is_equal_to.place(x=120,y=150)


def calculate_():
    text_box2.delete(0,END)
    mile = float(text_box1.get())
    ans = mile * 1.609
    text_box2.insert(END,f"{ans}")


button = tkinter.Button(text="Calculate",command=calculate_)
button.place(x=230,y=200)


screen.mainloop()



