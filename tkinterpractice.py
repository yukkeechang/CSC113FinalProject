import tkinter
from tkinter import *
from tkinter import ttk
import turtle
import random
###module for calcualting text file character percentages
import percentages

###main window that surrounds the interface
root = Tk()

###used to surround other widgits
frame = Frame(root)
canvas = Canvas(master=root, width=500, height=500)

###LABEL
labelText = StringVar()
labelText.set("Enter a number")
###the frame is where you wanna put the label in
label = Label(frame, textvariable=labelText)
label.pack()

###ENTRY
entry = Entry(root)
entry.pack()
def cb() :
    print(entry.get())

###BUTTON
button = Button(frame, text="Submit", command=cb)
###pack (placing) and positions widgits inside the window (order matters)
button.pack()
frame.pack()
canvas.pack()

###getting dictionary of character and their percentage frequency from percentages.py module
percents = percentages.getPercentages()

###puts turtle module in tkinter using canvas method
turt = turtle.RawTurtle(canvas)

###set position for piechart
turt.sety(-100)

turt.penup()
numStr = entry.get()
if (numStr is '') :
    ###if no input provided, set the default to 1
    numStr = 1
else :
    numStr = entry.get()

print("num string: ", numStr)
turt.pendown()


for i in percents :
    ###color generator - ensures different color for each slice
    ranColor = "#%06x" % random.randint(0, 0xFFFFFF)

    ###filling color for pie slices
    turt.fillcolor(ranColor)
    turt.begin_fill()

    ###dividing circle for pie slices
    turt.circle(100, percents[i]*360/100)

    position = turt.position()
    turt.goto(0, 0)
    turt.end_fill()
    turt.setposition(position)

#keeps root window visible and main program running till we close it
root.mainloop()
