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

def printChart() :

    ###getting dictionary of character and their percentage frequency from percentages.py module

    ###puts turtle module in tkinter using canvas method
    turt = turtle.RawTurtle(canvas)
    ###set position for piechart
    turt.sety(-100)
    numStr = entry.get()
    if (numStr is '') :
        ###if no input provided, set the default to 1
        numStr = 1
    else :
        numStr = int(entry.get())
    print("num string: ", numStr)
    percents = percentages.recalculatePercentages(numStr)

    #def recalculatePercentages(numStr) :


    ###drawing the chart! Where the magic happens
    for i in percents :
        ###color generator - ensures different hex number for each slice
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

    turt.sety(-100)
    ###Adding label to pie slices

    for k, percent in percents.items() :
        turt.circle(100, percent*360/100/2)
        turt.write(k, align="right", font="Avenir")
        turt.write('%s %%' %percent, align="left", font="Avenir")
        turt.circle(100, percent*360/100/2)

    ###COMMENT THIS OUT if you don't want the pie chart to disapear immediately
    turt.reset()


###BUTTON
button = Button(frame, text="Submit", command=printChart)
###pack (placing) and positions widgits inside the window (order matters)
button.pack()
frame.pack()
canvas.pack()



###keeps root window visible and main program running till we close it
root.mainloop()
