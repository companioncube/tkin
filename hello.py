from tkinter import *

root = Tk()

e=Entry(root, width=50, bg="blue", borderwidth=5)
e.insert(0, "Enter your name: ")
def myClick():
    myLabel1 = Label(root, text=e.get())
    myLabel1.grid(row=0, column=0)

myLabel2 = Label(root, text="Bye World!")
myLabel3 = Label(root, text="B World!")
myButton = Button(root, text="Click me",padx=50,pady=50,command=myClick,fg="red",bg="green")

myButton.grid(row=2, column=0)

myLabel2.grid(row=1, column=1)
myLabel3.grid(row=1, column=2)
e.grid(row=2, column=1)





root.mainloop()