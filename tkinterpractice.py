import tkinter
from tkinter import *
from tkinter import ttk

#main window that surrounds the interface
root = Tk()
#part 1
# root.title("First GUI")
# #grid is layout manager
# ttk.Button(root, text= "button!").grid()


#part2
#used to surround other widgits
frame = Frame(root)

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

numString = entry.get()
print(numString)
#keeps root window visible and main program running till we close it
root.mainloop()
