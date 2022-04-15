from tkinter import *

class student :
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",font=("Times new roman",40,"bold"),bg="light blue",fg="black")
        title.pack(side=TOP)


root=Tk()
ob=student(root)
root.mainloop()