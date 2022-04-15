from cProfile import label
from tkinter import *

from matplotlib.pyplot import text
from mysqlx import Column

class student :
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("Times new roman",40,"bold"),bg="light blue",fg="black")
        title.pack(side=TOP,fill=X)


        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light green")  # to customize the left frame
        Manage_Frame.place(x=15,y=100,width=450,height=560)



        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="light green")   # to customize the right frame
        Detail_Frame.place(x=500,y=100,width=825,height=560)

        #left frame inner details
        m_title=Label(Manage_Frame,text="Manager Students",bg="light green",fg="black",font=("Times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)


        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="light green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky='w')

        txt_roll=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        lbl_name=Label(Manage_Frame,text="Name",bg="light green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')

        lbl_name=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        lbl_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')

        lbl_Email=Label(Manage_Frame,text="Email",bg="light green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky='w')

        lbl_Email=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        lbl_Email.grid(row=3,column=1,pady=10,padx=20,sticky='w')
        






root=Tk()
ob=student(root)
root.mainloop()