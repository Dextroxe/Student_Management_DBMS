from tkinter import *

class student :
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("Times new roman",40,"bold"),bg="light blue",fg="black")
        title.pack(side=TOP,fill=X)


        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light green")
        Manage_Frame.place(x=20,y=100,width=450,height=560)


        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light green")
        Detail_Frame.place(x=500,y=100,width=825,height=560)







root=Tk()
ob=student(root)
root.mainloop()