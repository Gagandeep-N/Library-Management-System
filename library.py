from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime
from requests import delete

from torch import frac

class libraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")

        #=====Variable=====#
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()






        lbltitle = Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side="top",fill=X)

        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)


        #=====Data Frame Left=====#
        DataFrameLeft = LabelFrame(frame,text="LIBRARY MEMBERSHIP INFORMATION",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember = Label(DataFrameLeft,text="Member Type",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblMember.grid(row=0,column=0,sticky=W)
        comboMember = ttk.Combobox(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.member_var,width=29,state="readonly")
        comboMember["value"] = ("Admin", "Student", "Professor")
        comboMember.grid(row=0,column=1)

        lblPRN_No = Label(DataFrameLeft,text="PRN No",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No = Entry(DataFrameLeft,font=("aerial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_No.grid(row=1,column=1)

        lblTitle = Label(DataFrameLeft,text="ID No",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle = Entry(DataFrameLeft,font=("aerial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName = Label(DataFrameLeft,text="First Name",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName = Entry(DataFrameLeft,font=("aerial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName = Label(DataFrameLeft,text="Last Name",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName = Entry(DataFrameLeft,font=("aerial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1 = Label(DataFrameLeft,text="Address1",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1 = Entry(DataFrameLeft,font=("aerial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2 = Label(DataFrameLeft,text="Address2",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2 = Entry(DataFrameLeft,font=("aerial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode = Label(DataFrameLeft,text="Post Code",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode = Entry(DataFrameLeft,font=("aerial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile = Label(DataFrameLeft,text="Mobile",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile = Entry(DataFrameLeft,font=("aerial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId = Label(DataFrameLeft,text="Book ID",font=("aerial",12,"bold"),padx=2,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId = Entry(DataFrameLeft,font=("aerial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle = Label(DataFrameLeft,text="Book Title",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle = Entry(DataFrameLeft,font=("aerial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor = Label(DataFrameLeft,text="Author Name",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor = Entry(DataFrameLeft,font=("aerial",12,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed = Label(DataFrameLeft,text="Date Borrowed",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft,font=("aerial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue = Label(DataFrameLeft,text="Date Due",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue = Entry(DataFrameLeft,font=("aerial",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook = Label(DataFrameLeft,text="Days On Book",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft,font=("aerial",12,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine = Label(DataFrameLeft,text="Late Return Fine",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft,font=("aerial",12,"bold"),textvariable=self.lateratefine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue = Label(DataFrameLeft,text="Date Over Due",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue = Entry(DataFrameLeft,font=("aerial",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice = Label(DataFrameLeft,text="Actual Price",font=("aerial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice = Entry(DataFrameLeft,font=("aerial",12,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)

        #=====Data Frame Right=====#
        DataFrameRight = LabelFrame(frame,text="BOOK DETAILS",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("aerial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox = Text(DataFrameRight,font=("aerial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollBar = Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0,column=1,sticky="ns")

        listBooks = ['Programming in Python', 'DataStructures And Algorithms', 'Machine Learning','Artificial Intelligence', 'Computer Networks','DBMS','C programming','Operating System','Operation Research','C++','Java Programming','Analysis of Algorithms','Messi Biography','Cryptography','Spoken English','Compiler Design','Data Mining']
        
        def selectBook(event):
            index=listBox.curselection()
            value = listBox.get(index[0])
            
            x=value
            if (x=="DataStructures And Algorithms"):
                self.bookid_var.set("BKID002")
                self.booktitle_var.set("DataStructures And Algorithms")
                self.author_var.set("Jake")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 999")

            elif (x=="Programming in Python"):
                self.bookid_var.set("BKID001")
                self.booktitle_var.set("Programming in Python")
                self.author_var.set("Paul")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 799")

            elif (x=="Machine Learning"):
                self.bookid_var.set("BKID003")
                self.booktitle_var.set("Machine Learning")
                self.author_var.set("Mark")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 650")

            elif (x=="Artificial Intelligence"):
                self.bookid_var.set("BKID004")
                self.booktitle_var.set("Artificial Intelligence")
                self.author_var.set("Holland")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 1500")

            elif (x=="Computer Networks"):
                self.bookid_var.set("BKID005")
                self.booktitle_var.set("Computer Networks")
                self.author_var.set("Bush")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 1000")

            elif (x=="DBMS"):
                self.bookid_var.set("BKID006")
                self.booktitle_var.set("DBMS")
                self.author_var.set("Kailash")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 800")

            elif (x=="C programming"):
                self.bookid_var.set("BKID007")
                self.booktitle_var.set("C programming")
                self.author_var.set("Bush")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs. 1000")
            
            

        
        
        listBox = Listbox(DataFrameRight,font=("aerial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",selectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)



        #=====Buttons Frame=====#
        framebutton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=530,width=1530,height=60)

        btnAddData = Button(framebutton,command=self.add_data,text="Add Data",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnShowData = Button(framebutton,command=self.show_data,text="Developer",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnShowData.grid(row=0,column=1)

        btnUpdateData = Button(framebutton,command=self.update,text="Update",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnUpdateData.grid(row=0,column=2)

        btnDeleteData = Button(framebutton,command=self.delete,text="Delete",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnDeleteData.grid(row=0,column=3)

        btnResetData = Button(framebutton,command=self.reset,text="Reset",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnResetData.grid(row=0,column=4)

        btnExit = Button(framebutton,command=self.iexit,text="Exit",font=("aerial",12,"bold"),width=23,bg="blue",fg="white")
        btnExit.grid(row=0,column=5)




        #=====Information Frame=====#
        frameDetails = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameDetails.place(x=0,y=590,width=1530,height=210)

        tableFrame = Frame(frameDetails,bd=6,relief=RIDGE,bg="powder blue")
        tableFrame.place(x=0,y=2,width=1460,height=190)

        xscroll = ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(tableFrame,orient=VERTICAL)

        self.library_table = ttk.Treeview(tableFrame,column=("MemberType","PRNNo","Title","FirstName","LastName","Address1","Address2","PostID","Mobile","BookID","BookTitle","Author","DateBorrowed","DateDue","Days","LateReturnFine","DateOverDue","FinalPrice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("MemberType",text="Member Type")
        self.library_table.heading("PRNNo",text="PRN No.")
        self.library_table.heading("Title",text="Title")
        self.library_table.heading("FirstName",text="First Name")
        self.library_table.heading("LastName",text="Last Name")
        self.library_table.heading("Address1",text="Address1")
        self.library_table.heading("Address2",text="Address2")
        self.library_table.heading("PostID",text="Post ID")
        self.library_table.heading("Mobile",text="Mobile Number")
        self.library_table.heading("BookID",text="Book ID")
        self.library_table.heading("BookTitle",text="Book Title")
        self.library_table.heading("Author",text="Author")
        self.library_table.heading("DateBorrowed",text="Borrowed Date")
        self.library_table.heading("DateDue",text="Date Due")
        self.library_table.heading("Days",text="Days On Book")
        self.library_table.heading("LateReturnFine",text="Late Return Fine")
        self.library_table.heading("DateOverDue",text="Date Over Due")
        self.library_table.heading("FinalPrice",text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("MemberType",width=100)
        self.library_table.column("PRNNo",width=100)
        self.library_table.column("Title",width=100)
        self.library_table.column("FirstName",width=100)
        self.library_table.column("LastName",width=100)
        self.library_table.column("Address1",width=100)
        self.library_table.column("Address2",width=100)
        self.library_table.column("PostID",width=100)
        self.library_table.column("Mobile",width=100)
        self.library_table.column("BookID",width=100)
        self.library_table.column("BookTitle",width=100)
        self.library_table.column("Author",width=100)
        self.library_table.column("DateBorrowed",width=100)
        self.library_table.column("DateDue",width=100)
        self.library_table.column("Days",width=100)
        self.library_table.column("LateReturnFine",width=100)
        self.library_table.column("DateOverDue",width=100)
        self.library_table.column("FinalPrice",width=100)

        self.fetch_data()

    def add_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="library")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finalprice_var.get()
                                                                                                                ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record Added Successfully!")

    def update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="library")
        my_cursor = conn.cursor()
        my_cursor.execute("update detail set MemberType=%s,PRN_No=%s,ID_No=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostCode=%s,Mobile=%s,Book_ID=%s,BookTitle=%s,Author=%s,DateOfBorrow=%s,DateDue=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDue=%s,ActualPrice=%s where PRN_No=%s",(
                                                                                                                                                                                                                                                                                                    self.member_var.get(),
                                                                                                                                                                                                                                                                                                    self.id_var.get(),
                                                                                                                                                                                                                                                                                                    self.firstname_var.get(),
                                                                                                                                                                                                                                                                                                    self.lastname_var.get(),
                                                                                                                                                                                                                                                                                                    self.address1_var.get(),
                                                                                                                                                                                                                                                                                                    self.address2_var.get(),
                                                                                                                                                                                                                                                                                                    self.postcode_var.get(),
                                                                                                                                                                                                                                                                                                    self.mobile_var.get(),
                                                                                                                                                                                                                                                                                                    self.bookid_var.get(),
                                                                                                                                                                                                                                                                                                    self.booktitle_var.get(),
                                                                                                                                                                                                                                                                                                    self.author_var.get(),
                                                                                                                                                                                                                                                                                                    self.dateborrowed_var.get(),
                                                                                                                                                                                                                                                                                                    self.datedue_var.get(),
                                                                                                                                                                                                                                                                                                    self.daysonbook_var.get(),
                                                                                                                                                                                                                                                                                                    self.lateratefine_var.get(),
                                                                                                                                                                                                                                                                                                    self.dateoverdue_var.get(),
                                                                                                                                                                                                                                                                                                    self.finalprice_var.get(),
                                                                                                                                                                                                                                                                                                    self.prn_var.get()
                                                                                                                                                                                                                                                                                                 ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Record has been updated!")                                                                                                    

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="library")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from detail")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def show_data(self):
        self.txtBox.insert(END,"This mini project is developed by \nGagandeep N.\n\nI am an Information Science and \nEngineering student.\n\nI like to code in python.")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.lateratefine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")

    def iexit(self):
        iexit = tkinter.messagebox.askyesno("LIBRARY MANAGEMENT SYSTEM","Do you want to exit?")
        if iexit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error","Couldn't delete...sorry!!")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="library")
            my_cursor = conn.cursor()
            query = "delete from detail where PRN_No=%s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query,value)


            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Record has been deleted")


        

if __name__ == '__main__':
    root=Tk()
    obj = libraryManagementSystem(root)
    root.mainloop()