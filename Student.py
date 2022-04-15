from math import comb
from tkinter import *
from tkinter import ttk
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

         # roll number part
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="light green",fg="black",font=("Sans-serif",20,"bold")) 
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky='w')

        txt_roll=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        #name part
        lbl_name=Label(Manage_Frame,text="Name",bg="light green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')

        txt_name=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')


        # Email part
        lbl_Email=Label(Manage_Frame,text="Email",bg="light green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky='w')

        txt_Email=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky='w')


        #Gender part
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="light green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky='w')

        combo_gender=ttk.Combobox(Manage_Frame,font=("Times new roman",14,"bold"))
        combo_gender['values']=("Female","Male","Other")
        combo_gender.grid(row=4,column=1,padx=10,pady=20,sticky='w')


        #Contact part
        lbl_Contact=Label(Manage_Frame,text="Contact",bg="light green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky='w')

        txt_Contact=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')

          #Date of Birth part
        lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="light green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky='w')

        txt_DOB=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky='w')

          #Address part
        lbl_Address=Label(Manage_Frame,text="Address",bg="light green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky='w')

        txt_Address=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky='w')
        
        






root=Tk()
ob=student(root)
root.mainloop()