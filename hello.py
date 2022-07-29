from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Bye World!")
myLabel3 = Label(root, text="B World!")
myButton = Button(root, text="Click me",state=DISABLED,padx=50)

myButton.grid(row=2, column=0)
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=1, column=2)





root.mainloop()