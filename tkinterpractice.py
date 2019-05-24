import tkinter
from tkinter import *
from tkinter import ttk
import turtle
import random


#main window that surrounds the interface
root = Tk()
#part 1
# root.title("First GUI")
# #grid is layout manager
# ttk.Button(root, text= "button!").grid()


#part2
#used to surround other widgits
frame = Frame(root)
canvas = Canvas(master=root, width=500, height=500)

#LABEL
labelText = StringVar()
labelText.set("Enter a number")
#the frame is where you wanna put the label in
label = Label(frame, textvariable=labelText)
label.pack()

#ENTRY
entry = Entry(root)
entry.pack()
def cb() :
    print(entry.get())

#BUTTON
button = Button(frame, text="Submit", command=cb)
#pack positions widgits inside the window (order matters)
button.pack()


frame.pack()
canvas.pack()

numString = entry.get()
print(numString)


#turt = turtle.Turtle()
###Puts turtle module in tkinter using canvas method
turt = turtle.RawTurtle(canvas)

###sets pen state for turtle. Will move around but not draw anything
#turt.penup()
#turt = turtle.Turtle()





dict = { "a":10, "b":10, "c":10, "d":10, "e":10, "f": 10, "g": 10}
turt.sety(-100)
j=1

#todo:set j to the number inputted in tkinter
while(j < 6) :
    for i in dict :
        ###color generator
        ranColor = "#%06x" % random.randint(0, 0xFFFFFF)
        print("i ", i)
        turt.fillcolor(ranColor)
        j += 1
        turt.begin_fill()
        turt.circle(100, dict[i]*360/100)
        position = turt.position()
        turt.goto(0, 0)
        turt.end_fill()
        turt.setposition(position)


#keeps root window visible and main program running till we close it
root.mainloop()
