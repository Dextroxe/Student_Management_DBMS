
from tkinter import *
from tkinter import ttk

class student :
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("Times new roman",40,"bold"),bg="pale green",fg="black")
        title.pack(side=TOP,fill=X)



       #---------------RIGHT Frame----------------------
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="green")    # to customize the COLOR OR FONT OF right frame
        Manage_Frame.place(x=20,y=100,width=450,height=660)

        m_title=Label(Manage_Frame,text="Manager Students",bg="green",fg="black",font=("Times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)


         # roll number part
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="green",fg="black",font=("Sans-serif",20,"bold")) 
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky='w')

        txt_roll=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        #name part
        lbl_name=Label(Manage_Frame,text="Name",bg="green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')

        txt_name=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')


        # Email part
        lbl_Email=Label(Manage_Frame,text="Email",bg="green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky='w')

        txt_Email=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky='w')


        #Gender part
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky='w')

        combo_gender=ttk.Combobox(Manage_Frame,font=("Times new roman",14,"bold"))
        combo_gender['values']=("Female","Male","Other")
        combo_gender.grid(row=4,column=1,padx=10,pady=20,sticky='w')


        #Contact part
        lbl_Contact=Label(Manage_Frame,text="Contact",bg="green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky='w')

        txt_Contact=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')

        #Date of Birth part
        lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky='w')

        txt_DOB=Entry(Manage_Frame,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky='w')

        #Address part
        lbl_Address=Label(Manage_Frame,text="Address",bg="green",fg="black",font=("Sans-serif",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky='w')

        txt_Address=Text(Manage_Frame,width=20,height=4,font=("Times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky='w')
        
        #----------Buttons Frame -----------------

        btn_frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="green")
        btn_frame.place(x=10,y=580,width=416)

        addbtn=Button(btn_frame,text="ADD",width=8).grid(row=8,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="UPDATE",width=8).grid(row=8,column=1,padx=10,pady=10)
        deletebtn=Button(btn_frame,text="DELETE",width=8).grid(row=8,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="CLEAR",width=8).grid(row=8,column=3,padx=10,pady=10)


       #---------------LEFT Frame----------------------
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="green")    # to customize the COLOR OR FONT OF right frame
        Detail_Frame.place(x=500,y=100,width=930,height=660)    

        lbl_search=Label(Detail_Frame,text="Search by",bg="green",fg="black",font=("Times new roman",20,"bold"))
        lbl_search.grid(row=0,column=1,pady=10,padx=10,sticky='w')

        combo_search=ttk.Combobox(Detail_Frame,width=15,font=("Times new roman",14,"bold"))
        combo_search['values']=("Roll no.","Name","Contact")
        combo_search.grid(row=0,column=2,padx=20,pady=10)

        txt_search=Entry(Detail_Frame,font=("Times new roman",14,"bold"),bd=6,relief=GROOVE)
        txt_search.grid(row=0,column=3,pady=10,padx=20,sticky='w')
        
        searchbtn=Button(Detail_Frame,text="SEARCH",width=12).grid(row=0,column=4,padx=10,pady=10)
        shawallbtn=Button(Detail_Frame,text="SHOW ALL",width=12).grid(row=0,column=5,padx=10,pady=10)



        #--------------Table Frame-------------------

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="green")  
        Table_Frame.place(x=10,y=70,width=900,height=500)  
        

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        
        Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("roll",text="Roll No.")
        Student_table.heading("name",text="Name")
        Student_table.heading("email",text="Email")
        Student_table.heading("gender",text="Gender")
        Student_table.heading("contact",text="Cpntact")
        Student_table.heading("dob",text="D.O.B")
        Student_table.heading("Address",text="Address")
        Student_table['show']='headings'
        Student_table.column("roll",width=100)
        Student_table.column("name",width=100)
        Student_table.column("email",width=100)
        Student_table.column("gender",width=100)
        Student_table.column("contact",width=100)
        Student_table.column("dob",width=100)
        Student_table.column("Address",width=150)

        Student_table.pack(fill=BOTH,expand=1)


        #more content 

root=Tk()
ob=student(root)
root.mainloop()