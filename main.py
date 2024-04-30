from tkinter import *
import sqlite3
from tkinter import messagebox

# database that contains username and passwords of librarians
login=sqlite3.connect("admin.db")
l=login.cursor()

med=sqlite3.connect("Library.db")
m=med.cursor()

def open_win():
    global apt
    apt = Tk()
    apt.state('zoomed')  # Maximizes the window to fit the screen
    apt.configure(bg='white')
    apt.title('Login')
    # FOR SECOND PAGE

# TITLE
    Label(apt, text="WELCOME", font=('times new roman', 45,), fg='blue',bg='white').grid(row=1, column=1)
    Label(apt, text="LIBRARY MANAGEMENT SYSTEM", font=('times new roman', 25), fg='red',bg='white').grid(row=2, column=1)
    Label(apt, text="When in doubt, read a Book", font=('times new roman', 15,), fg='green',bg='white').grid(row=3, column=1,pady=5)
    Label(apt, text="-"*150, font=('ariel', 15,), fg='green',bg='white').grid(row=4, column=1, pady=5)

    Label(apt, text="LIBRARY MEMBERS", bg='black', fg='white', font=('ariel', 12),width=25).grid(row=8, column=0,padx=10,pady=5)
    Button(apt, text='View Members', width=25, bg='green', font=('ariel', 12), fg='white', command=view_members).grid(row=9, column=0,padx=10,pady=5)
    Button(apt, text='Update details of any member', bg='green', font=('ariel', 12), fg='white', width=25, command=update_member).grid(row=10, column=0,padx=10,pady=5)
    Button(apt, text='Remove details of a person', bg='red', font=('ariel', 12), fg='white', width=25, command=del_member).grid(row=11, column=0,padx=10,pady=5)
    Button(apt, text='Insert details of new member', bg='red', font=('ariel', 12), fg='white', width=25,command=insert_member).grid(row=12, column=0, padx=10, pady=5)
    Button(apt, text='Search details of a member', bg='red', font=('ariel', 12), fg='white', width=25,command=search_member).grid(row=13, column=0, padx=10, pady=5)


# TO ACCESS THE TABLE CONTAINING INFORMATION OF BOOKS AVAILABLE IN LIBRARIAN
    Label(apt, text="BOOK RECORDS", bg='black', font=('ariel', 12), fg='white',width=25).grid(row=8, column=1,padx=10,pady=5)
    Button(apt, text='View Books', width=25, bg='blue', font=('ariel', 12), fg='white', command=view_book).grid(row=9,column=1,padx=10,pady=5)
    Button(apt, text='Update Book details', bg='blue', fg='white', font=('ariel', 12), width=25, command=update_avail_book).grid(row=10,column=1,padx=10,pady=5)
    Button(apt, text='Remove a Book', bg='red', fg='white', font=('ariel', 12), width=25, command=del_avail_book).grid(row=11, column=1,padx=10,pady=5)
    Button(apt, text='Insert a new Book', bg='red', fg='white', font=('ariel', 12), width=25,command=insert_book_avail).grid(row=12, column=1, padx=10, pady=5)
    Button(apt, text='Search Available Books', bg='red', fg='white', font=('ariel', 12), width=25,command=search_avail_book).grid(row=13, column=1, padx=10, pady=5)
    Button(apt, text='QUIT', bg='red', fg='white', font=('ariel', 12), width=25,command=apt.destroy).grid(row=14, column=1, padx=10, pady=30)

# TO ACCESS THE TABLE CONTAINING INFORMATION OF ISSUED BOOKS IN LIBRARY
    Label(apt, text="ISSUED BOOK RECORDS", bg='black', font=('ariel', 12), fg='white', width=25).grid(row=8, column=2,padx=10, pady=5)
    Button(apt, text='View Issued Books', width=25, bg='yellow', font=('ariel', 12), fg='black',command=view_issued_books).grid(row=9, column=2, padx=10,pady=5)
    Button(apt, text='Update Issued Book details', width=25, bg='yellow', font=('ariel', 12), fg='black',command=update_issued_book).grid(row=10,column=2,padx=10, pady=5)
    Button(apt, text='Remove Issued Book', width=25, bg='yellow', font=('ariel', 12), fg='black',command=del_issued_book).grid(row=11, column=2, padx=10, pady=5)
    Button(apt, text='Insert a new Issued Book', width=25, bg='red', font=('ariel', 12), fg='black',command=insert_book_issued).grid(row=12, column=2, padx=10, pady=5)
    Button(apt, text='Search Issued Books', width=25, bg='red', font=('ariel', 12), fg='black', command=search_issued_book).grid(row=13,column=2,padx=10,pady=5)



    apt.mainloop()

def back_d():
    global d
    d.destroy()
    open_win()

def back_w():
    global d,w
    d.destroy()
    w.withdraw()
    open_win()


#view the table consisting of details of all the members
def view_members():
    apt.destroy()
    global d
    d = Tk()
    d.title("MEMBER DETAILS")
    d.configure(bg='white')
    Label(d, text="Member_id ",bg='white').grid(row=0, column=0, ipadx=12)
    Label(d, text="Name ",bg='white').grid(row=0, column=1, ipadx=12)
    Label(d, text="Contact ",bg='white').grid(row=0, column=2, ipadx=12)
    Label(d, text="Address ",bg='white').grid(row=0, column=3, ipadx=12)
    Label(d, text="Joining_date ", bg='white').grid(row=0, column=4, ipadx=12)
    l.execute("select * from member_details")
    i = 0
    for student in l:
        for j in range(len(student)):
            e = Entry(d, width=30, fg='black',bg='white')
            e.grid(row=i + 1, column=j)
            e.insert(END, student[j])
        i = i + 1
    Button(d,text="BACK",bg='black',fg='white',font=('ariel',12),width=15,command=back_d).grid(row=i+1,column=0,sticky=SW)
    d.mainloop()

# updating the member table
def modify_member():
    global d,e1,e5,e6,e7,e8,e9
    a=e5.get()
    b=e6.get()
    c=e7.get()
    d=e8.get()
    e=e9.get()
    f=e1.get()

    l.execute("UPDATE member_details SET Member_id='"+a+"',Name='"+b+"',Contact='"+c+"',Address='"+d+"',Joining_date='"+e+"'  where Member_id='"+f+"' ")
    login.commit()
    messagebox.showinfo("DONE","Record succesfully modified!")
    d.withdraw()
    open_win()


def update_member():
    apt.destroy()
    global d,e1,e5,e6,e7,e8,e9
    d=Tk()
    d.geometry('1000x130')
    d.title("UPDATING")
    d.configure(bg='white')
    Label(d, text="OLD Member_id ",bg='white').grid(row=0, column=0, ipadx=12)
    e1 =Entry(d)
    e1.grid(row=0, column=1)
    # new data:
    Label(d, text="NEW Member_id ",bg='white').grid(row=0, column=3, ipadx=12)
    e5 = Entry(d)
    e5.grid(row=0, column=4)
    Label(d, text="NEW Name ",bg='white').grid(row=1, column=3, ipadx=12)
    e6 =Entry(d)
    e6.grid(row=1, column=4)
    Label(d, text="NEW Contact ",bg='white').grid(row=2, column=3, ipadx=12)
    e7 = Entry(d)
    e7.grid(row=2, column=4)
    Label(d, text="NEW Address ",bg='white').grid(row=3, column=3, ipadx=12)
    e8 = Entry(d)
    e8.grid(row=3, column=4)
    Label(d, text="NEW Joining_date ", bg='white').grid(row=4, column=3, ipadx=12)
    e9 = Entry(d)
    e9.grid(row=4, column=4)

    Button(d, text="SET", fg='white', width=30, bg='red', command=modify_member).grid(row=8, column=2)
    Button(d, text="BACK", fg='white', width=30, bg='black', command=back_d).grid(row=8, column=3)


    d.mainloop()

# deleting a record from member's table
def del_m():
    global  d,a1
    l.execute("DELETE from member_details where Member_id='" + a1.get() + "'")
    login.commit()
    messagebox.showinfo("DONE", "Record succesfully deleted!")
    d.withdraw()
    open_win()


def del_member():
    apt.destroy()
    global d,a1
    d = Tk()
    d.configure(bg='white')
    d.geometry('400x100')
    d.title("DELETE RECORD")
    Label(d, text="MEMBER ID ",bg='white').grid(row=1, column=0, ipadx=12)
    a1 =Entry(d)
    a1.grid(row=1, column=1)
    Button(d,text="DELETE",command=del_m,bg='red',fg='white',width=14).grid(row=2,column =0 )
    Button(d, text="BACK", command=back_d, bg='black', fg='white', width=14).grid(row=2, column=1)
    d.mainloop()



# Inserting new records in the member's table
def add_member():
    global d,id,name,contact,add,doj
    e1=id.get()
    e2=name.get()
    e3=contact.get()
    e4=add.get()
    e5=doj.get()
    q=(e1,e2,e3,e4,e5)
    l.execute("INSERT INTO member_details VALUES (?,?,?,?,?)",q)
    login.commit()
    messagebox.showinfo("DONE", "Record succesfully added!")
    d.withdraw()
    open_win()

def insert_member():
    apt.destroy()
    global d,id,name,contact,add,doj
    d=Tk()
    d.configure(bg='white')
    d.title("ADD MEMBER")
    Label(d, text="Member_id ",bg='white').grid(row=0, column=0, ipadx=12)
    id=Entry(d)
    id.grid(row=0,column=1)
    Label(d, text="Name ",bg='white').grid(row=1, column=0, ipadx=12)
    name = Entry(d)
    name.grid(row=1, column=1)
    Label(d, text="Contact ",bg='white').grid(row=2, column=0, ipadx=12)
    contact = Entry(d)
    contact.grid(row=2, column=1)
    Label(d, text="Address ",bg='white').grid(row=3, column=0, ipadx=12)
    add = Entry(d)
    add.grid(row=3, column=1)
    Label(d, text="Joining_date ", bg='white').grid(row=4, column=0, ipadx=12)
    doj = Entry(d)
    doj.grid(row=4, column=1)

    Button(d, text="INSERT", fg='white', width=30, bg='red', command=add_member).grid(row=6 ,column=1,pady=5)
    Button(d, text="BACK", fg='white', width=30, bg='black', command=back_d).grid(row=6, column=2,pady=5)

    d.mainloop()
def search_m():
    global d,Member_id,w
    if d:
        d.withdraw()
    w=Tk()
    w.configure(bg='white')
    Label(d, text="Member_id ", bg='white').grid(row=0, column=0, ipadx=12)
    Label(d, text="Name ", bg='white').grid(row=0, column=1, ipadx=12)
    Label(d, text="Contact ", bg='white').grid(row=0, column=2, ipadx=12)
    Label(d, text="Address ", bg='white').grid(row=0, column=3, ipadx=12)
    Label(d, text="Joining_date ", bg='white').grid(row=0, column=4, ipadx=12)
    l.execute("select * from member_details where Member_id='"+Member_id.get()+"'  ")
    i = 0
    for student in l:
        for j in range(len(student)):
            e = Entry(w, width=30, fg='black',bg='white')
            e.grid(row=i + 1, column=j)
            e.insert(END, student[j])
        i = i + 1
    Button(w, text="BACK", bg='black', fg='white', font=('ariel', 12), width=15, command=back_w).grid(row=i + 1, column=0,sticky=SW)



def search_member():
    apt.destroy()
    global d,Member_id
    d=Tk()
    d.title("Search Staff")
    d.configure(bg='white')
    Label(d, text="Member_id ",bg='white').grid(row=0, column=0, ipadx=12)
    Member_id = Entry(d)
    Member_id.grid(row=0, column=1)
    Button(d, text="View", fg='white', width=30, bg='red', command=search_m).grid(row=6, column=1, pady=5)
    Button(d, text="BACK", fg='white', width=30, bg='black', command=back_d).grid(row=6, column=2, pady=5)

    d.mainloop()


#View available books table
def view_book():
    apt.destroy()
    global d
    d = Tk()
    d.title("BOOK DETAILS")
    d.configure(bg='white')
    Label(d, text="BOOK ISBN ",bg='white').grid(row=0, column=0, ipadx=5)
    Label(d, text="BOOK TITLE ",bg='white').grid(row=0, column=1, ipadx=5)
    Label(d, text="AUTHOR",bg='white').grid(row=0, column=2, ipadx=5)
    Label(d, text="CATEGORY ",bg='white').grid(row=0, column=3, ipadx=5)
    Label(d, text="PRICE ",bg='white').grid(row=0, column=4, ipadx=5)
    Label(d, text="COPIES ",bg='white').grid(row=0, column=5, ipadx=5)

    m.execute("select * from book")
    i = 0
    for student in m:
        for j in range(len(student)):
            e = Entry(d, width=30, fg='black',bg='white')
            e.grid(row=i + 1, column=j)
            e.insert(END, student[j])
        i = i + 1

    Button(d, text="BACK", bg='black', fg='white', font=('ariel', 12), width=15, command=back_d).grid(row=i + 1,column=0,sticky=SW)
    d.mainloop()

#Updating details of book available

def modify_book_avail():
    global d,oisbn,nisbn,ntitle,nauthor,ncategory,nprice,ncopy
    oldisbn=oisbn.get()
    newisbn=nisbn.get()
    newtitle=ntitle.get()
    newauthor=nauthor.get()
    newcategory=ncategory.get()
    newprice=nprice.get()
    newcopy=ncopy.get()
    m.execute("UPDATE book SET ISBN='"+newisbn+"', Title='"+newtitle+"', Author='"+newauthor+"', Category='"+newcategory+"', Price='"+newprice+"', Copies='"+newcopy+"' where ISBN='"+oldisbn+"' ")
    med.commit()
    messagebox.showinfo("DONE","Record successfully modified!")
    d.withdraw()
    open_win()


def update_avail_book():
    apt.destroy()
    global d,oisbn,nisbn,ntitle,nauthor,ncategory,nprice,ncopy
    d=Tk()
    d.configure(bg='white')
    d.title("UPDATING DETAILS")
    Label(d, text="OLD ISBN ",bg='white').grid(row=0, column=0, ipadx=12)
    oisbn = Entry(d)
    oisbn.grid(row=0, column=1)
    Label(d, text="OLD BOOK TITLE ",bg='white').grid(row=1, column=0, ipadx=12)
    otitle = Entry(d)
    otitle.grid(row=1, column=1)
    Label(d, text="OLD AUTHOR ",bg='white').grid(row=2, column=0, ipadx=12)
    oauthor = Entry(d)
    oauthor.grid(row=2, column=1)
    Label(d, text="OLD CATEGORY ",bg='white').grid(row=3, column=0, ipadx=12)
    ocategory= Entry(d)
    ocategory.grid(row=3, column=1)
    Label(d, text="OLD PRICE ",bg='white').grid(row=4, column=0, ipadx=12)
    oprice = Entry(d)
    oprice.grid(row=4, column=1)
    Label(d, text="OLD No. of copies ",bg='white').grid(row=5, column=0, ipadx=12)
    ocopy = Entry(d)
    ocopy.grid(row=5, column=1)

    # new data:
    Label(d, text="NEW ISBN ",bg='white').grid(row=0, column=3, ipadx=12)
    nisbn = Entry(d)
    nisbn.grid(row=0, column=4)
    Label(d, text="NEW TITLE ",bg='white').grid(row=1, column=3, ipadx=12)
    ntitle = Entry(d)
    ntitle.grid(row=1, column=4)
    Label(d, text="NEW Author ",bg='white').grid(row=2, column=3, ipadx=12)
    nauthor = Entry(d)
    nauthor.grid(row=2, column=4)
    Label(d, text="NEW Category ",bg='white').grid(row=3, column=3, ipadx=12)
    ncategory = Entry(d)
    ncategory.grid(row=3, column=4)
    Label(d, text="NEW Price ",bg='white').grid(row=4, column=3, ipadx=12)
    nprice = Entry(d)
    nprice.grid(row=4, column=4)
    Label(d, text="NEW No. of copies ",bg='white').grid(row=5, column=3, ipadx=12)
    ncopy = Entry(d)
    ncopy.grid(row=5, column=4)
    Button(d, text="SET", fg='white', width=30, bg='red', command=modify_book_avail).grid(row=8, column=2)
    Button(d, text="BACK", fg='white', width=30, bg='black', command=back_d).grid(row=8, column=3)

    d.mainloop()

#Deleting a book available
def del_book():
    global d,a1
    m.execute("DELETE from book where ISBN ='" + a1.get() + "'")
    med.commit()
    messagebox.showinfo("DONE", "Record succesfully deleted!")
    d.withdraw()
    open_win()

def del_avail_book():
    apt.destroy()
    global d,a1
    d = Tk()
    d.configure(bg='white')
    d.geometry('350x130')
    d.title("DELETING A BOOK")
    Label(d, text="ISBN",bg='white').grid(row=0, column=0, ipadx=9,padx=3,pady=15)
    a1 =Entry(d,width=24)
    a1.grid(row=0, column=1,padx=3,pady=15)
    Button(d, text="DELETE", command=del_book,bg='red',fg='white',width=20).grid(row=1, column=0,pady=15,padx=3)
    Button(d, text="BACK", command=back_d,bg='black',fg='white',width=20).grid(row=1, column=1,pady=15,padx=3)
    d.mainloop()


#inserting a new book to the available stock of books
def add_avail_book():
    global d,isbn,title,author,category,price,copy
    q=(isbn.get(),title.get(),author.get(),category.get(),price.get(),copy.get())
    m.execute("INSERT INTO book VALUES (?,?,?,?,?,?)",q)
    med.commit()
    messagebox.showinfo("DONE", "Record successfully added!")
    d.withdraw()
    open_win()


def insert_book_avail():
    apt.destroy()
    global d,isbn,title,author,category,price,copy
    d=Tk()
    d.configure(bg='white')
    d.title("ADDING NEW BOOK")
    Label(d, text="ISBN  ",bg='white').grid(row=0, column=0, ipadx=12)
    isbn = Entry(d)
    isbn.grid(row=0, column=1)
    Label(d, text="TITLE ",bg='white').grid(row=1, column=0, ipadx=12)
    title = Entry(d)
    title.grid(row=1, column=1)
    Label(d, text="Author ",bg='white').grid(row=2, column=0, ipadx=12)
    author = Entry(d)
    author.grid(row=2, column=1)
    Label(d, text="Category ",bg='white').grid(row=3, column=0, ipadx=12)
    category = Entry(d)
    category.grid(row=3, column=1)
    Label(d, text="Price ",bg='white').grid(row=4, column=0, ipadx=12)
    price = Entry(d)
    price.grid(row=4, column=1)
    Label(d, text="No. of copies ",bg='white').grid(row=5, column=0, ipadx=12)
    copy = Entry(d)
    copy.grid(row=5, column=1)


    Button(d, text="INSERT", command=add_avail_book, bg='red', fg='white', width=20).grid(row=8, column=0, pady=15, padx=3)
    Button(d, text="BACK", command=back_d, bg='black', fg='white', width=20).grid(row=8, column=1, pady=15, padx=3)
    d.mainloop()

#Search available books
def search_avail():
    global d,name,w
    if d:
        d.withdraw()

    w=Tk()
    w.configure(bg='white')
    Label(w, text="ISBN ",bg='white').grid(row=0, column=0, ipadx=5)
    Label(w, text="TITLE ",bg='white').grid(row=0, column=1, ipadx=5)
    Label(w, text="AUTHOR",bg='white').grid(row=0, column=2, ipadx=5)
    Label(w, text="CATEGORY ",bg='white').grid(row=0, column=3, ipadx=5)
    Label(w, text="PRICE ",bg='white').grid(row=0, column=4, ipadx=5)
    Label(w, text="COPIES ",bg='white').grid(row=0, column=5, ipadx=5)
    m.execute("select * from book where Title='"+name.get()+"' ")
    i = 0
    for student in m:
        for j in range(len(student)):
            e = Entry(w, width=30, fg='black',bg='white')
            e.grid(row=i + 1, column=j)
            e.insert(END, student[j])
        i = i + 1

    Button(w, text="BACK", bg='black', fg='white', font=('ariel', 12), width=15, command=back_w).grid(row=i + 1, column=0,
                                                                                                    sticky=SW)

    w.mainloop()


def search_avail_book():
    apt.destroy()
    global d,name
    d=Tk()
    d.configure(bg='white')
    d.title("Search Books Available")
    Label(d, text="Title",bg='white').grid(row=0, column=0, ipadx=5)
    name = Entry(d)
    name.grid(row=0, column=1)
    Button(d, text="View", fg='white', width=30, bg='red', command=search_avail).grid(row=3, column=1, pady=5)
    Button(d, text="BACK", fg='white', width=30, bg='black', command=back).grid(row=3, column=2, pady=5)

    d.mainloop()



#View issued books
def view_issued_books():
    apt.destroy()
    global d
    d = Tk()
    d.configure(bg='white')
    d.title("ISSUED BOOKS")
    Label(d, text="Issue_ID ",bg='white',fg='black').grid(row=0, column=0, ipadx=12)
    Label(d, text="Member ",bg='white',fg='black').grid(row=0, column=1, ipadx=12)
    Label(d, text="book_isbn ",bg='white',fg='black').grid(row=0, column=2, ipadx=12)
    Label(d, text="issue_date  ",bg='white',fg='black').grid(row=0, column=3, ipadx=12)
    Label(d, text="due_date  ", bg='white', fg='black').grid(row=0, column=4, ipadx=12)
    Label(d, text="Return_status ", bg='white', fg='black').grid(row=0, column=5, ipadx=12)
    m.execute("select * from book_issue")
    i = 0
    for student in m:
        for j in range(len(student)):
            e = Entry(d, width=30, fg='black',bg='white')
            e.grid(row=i + 1, column=j)
            e.insert(END, student[j])
        i = i + 1
    Button(d, text="BACK", bg='black', fg='white', font=('ariel', 12), width=15, command=back_d).grid(row=i + 1, column=0,sticky=SW)
    d.mainloop()


#Updating details of Issued books

def modify_book_issued():
    global d,old_issue_id,issue_id,member,book_isbn,issue_date,due_date,Return_status
    old_ID=old_issue_id.get()
    new_issue_id=issue_id.get()
    new_member=member.get()
    new_book_isbn=book_isbn.get()
    new_issue_date=issue_date.get()
    new_due_date=due_date.get()
    new_Return_status=Return_status.get()
    m.execute("UPDATE book_issue SET issue_id='"+new_issue_id+"', member='"+new_member+"', book_isbn='"+new_book_isbn+"', issue_date='"+new_issue_date+"', due_date='"+new_due_date+"', Return_status='"+new_Return_status+"' where issue_id='"+old_ID+"' ")
    med.commit()
    messagebox.showinfo("DONE","Record successfully modified!")
    d.withdraw()
    open_win()


def update_issued_book():
    apt.destroy()
    global d,old_issue_id,issue_id,member,book_isbn,issue_date,due_date,Return_status
    d=Tk()
    d.configure(bg='white')
    d.title("UPDATING DETAILS OF ISSUED BOOKS")
    Label(d, text="issue_id ",bg='white').grid(row=0, column=0, ipadx=12)
    old_issue_id = Entry(d)
    old_issue_id.grid(row=0, column=1)

    # new data:
    Label(d, text="NEW issue_id ",bg='white').grid(row=0, column=3, ipadx=12)
    issue_id = Entry(d)
    issue_id.grid(row=0, column=4)
    Label(d, text="NEW member ",bg='white').grid(row=1, column=3, ipadx=12)
    member = Entry(d)
    member.grid(row=1, column=4)
    Label(d, text="NEW book_isbn ",bg='white').grid(row=2, column=3, ipadx=12)
    book_isbn = Entry(d)
    book_isbn.grid(row=2, column=4)
    Label(d, text="NEW issue_date ",bg='white').grid(row=3, column=3, ipadx=12)
    issue_date = Entry(d)
    issue_date.grid(row=3, column=4)
    Label(d, text="NEW due_date ",bg='white').grid(row=4, column=3, ipadx=12)
    due_date = Entry(d)
    due_date.grid(row=4, column=4)
    Label(d, text="NEW Return_status ",bg='white').grid(row=5, column=3, ipadx=12)
    Return_status = Entry(d)
    Return_status.grid(row=5, column=4)
    Button(d, text="SET", fg='white', width=30, bg='red', command=modify_book_issued).grid(row=8, column=2)
    Button(d, text="BACK", fg='white', width=30, bg='black', command=back_d).grid(row=8, column=3)

    d.mainloop()


#Deleting a ISSUED BOOK
def del_book_issued():
    global d,a1
    m.execute("DELETE from book_issue where issue_id ='" + a1.get() + "'")
    med.commit()
    messagebox.showinfo("DONE", "Record succesfully deleted!")
    d.withdraw()
    open_win()

def del_issued_book():
    apt.destroy()
    global d,a1
    d = Tk()
    d.configure(bg='white')
    d.geometry('350x130')
    d.title("DELETING AN ISSUED BOOK")
    Label(d, text="issue_id",bg='white').grid(row=0, column=0, ipadx=9,padx=3,pady=15)
    a1 =Entry(d,width=24)
    a1.grid(row=0, column=1,padx=3,pady=15)
    Button(d, text="DELETE", command=del_book_issued,bg='red',fg='white',width=20).grid(row=1, column=0,pady=15,padx=3)
    Button(d, text="BACK", command=back_d,bg='black',fg='white',width=20).grid(row=1, column=1,pady=15,padx=3)
    d.mainloop()

#inserting a new book to the Issued stock of books
def add_issued_book():
    global d,issue_id,member,book_isbn,issue_date,due_date,Return_status
    q=(issue_id.get(),member.get(),book_isbn.get(),issue_date.get(),due_date.get(),Return_status.get())
    m.execute("INSERT INTO book_issue VALUES (?,?,?,?,?,?)",q)
    med.commit()
    messagebox.showinfo("DONE", "Record successfully added!")
    d.withdraw()
    open_win()


def insert_book_issued():
    apt.destroy()
    global d,issue_id,member,book_isbn,issue_date,due_date,Return_status
    d=Tk()
    d.configure(bg='white')
    d.title("ADDING NEW BOOK")
    Label(d, text="issue_id  ",bg='white').grid(row=0, column=0, ipadx=12)
    issue_id = Entry(d)
    issue_id.grid(row=0, column=1)
    Label(d, text="member ",bg='white').grid(row=1, column=0, ipadx=12)
    member = Entry(d)
    member.grid(row=1, column=1)
    Label(d, text="book_isbn ",bg='white').grid(row=2, column=0, ipadx=12)
    book_isbn = Entry(d)
    book_isbn.grid(row=2, column=1)
    Label(d, text="issue_date ",bg='white').grid(row=3, column=0, ipadx=12)
    issue_date = Entry(d)
    issue_date.grid(row=3, column=1)
    Label(d, text="due_date ",bg='white').grid(row=4, column=0, ipadx=12)
    due_date = Entry(d)
    due_date.grid(row=4, column=1)
    Label(d, text="Return_status ",bg='white').grid(row=5, column=0, ipadx=12)
    Return_status = Entry(d)
    Return_status.grid(row=5, column=1)


    Button(d, text="INSERT", command=add_issued_book, bg='red', fg='white', width=20).grid(row=8, column=0, pady=15, padx=3)
    Button(d, text="BACK", command=back_d, bg='black', fg='white', width=20).grid(row=8, column=1, pady=15, padx=3)
    d.mainloop()

#Search issued books

def search_issued():
    global d,issue_id,w
    d.withdraw()
    w=Tk()
    w.configure(bg='white')
    Label(d, text="Issue_ID ", bg='white', fg='black').grid(row=0, column=0, ipadx=12)
    Label(d, text="Member ", bg='white', fg='black').grid(row=0, column=1, ipadx=12)
    Label(d, text="book_isbn ", bg='white', fg='black').grid(row=0, column=2, ipadx=12)
    Label(d, text="issue_date  ", bg='white', fg='black').grid(row=0, column=3, ipadx=12)
    Label(d, text="due_date  ", bg='white', fg='black').grid(row=0, column=4, ipadx=12)
    Label(d, text="Return_status ", bg='white', fg='black').grid(row=0, column=5, ipadx=12)
    m.execute("select * from book_issue where issue_id='"+issue_id.get()+"' ")
    i = 0
    for student in m:
        for j in range(len(student)):
            e = Entry(w, width=30, fg='black',bg='white')
            e.grid(row=i + 1, column=j)
            e.insert(END, student[j])
        i = i + 1

    Button(w, text="BACK", bg='black', fg='white', font=('ariel', 12), width=15, command=back_w).grid(row=i + 1, column=0,
                                                                                                    sticky=SW)
    w.mainloop()

def search_issued_book():
    apt.destroy()
    global d,issue_id
    d=Tk()
    d.configure(bg='white')
    d.title("Search Books Available")
    Label(d, text="issue_id",bg='white').grid(row=0, column=0, ipadx=5)
    issue_id = Entry(d)
    issue_id.grid(row=0, column=1)
    Button(d, text="View", fg='white', width=30, bg='red', command=search_issued).grid(row=3, column=1, pady=5)
    Button(d, text="BACK", fg='white', width=30, bg='black', command=back_d).grid(row=3, column=2, pady=5)

    d.mainloop()




#LOGIN PAGE
def again():
    global un, pwd, flag, root, apt
    root = Tk()
    root.geometry('720x400')
    root.configure(bg='white')
    root.title('LOGIN')
    Label(root, text="WELCOME", font=('ariel', 45,), fg='blue',bg='white').grid(row=3, column=1)
    Label(root, text="LIBRARY MANAGEMENT SYSTEM", font=('ariel', 25,), fg='red',bg='white').grid(row=4, column=1)
    Label(root, text="When in doubt, read a Book", font=('ariel', 17,), fg='green',bg='white').grid(row=5, column=1)

    Label(root, text='----------------------------------------------------------', font=('ariel', 15,),bg='white' ).grid(row=7,column=1,columnspan=2)
    Label(root, text='Username', font=('ariel', 15,),bg='white').grid(row=8, column=0)
    un = Entry(root, width=30)
    un.grid(row=8, column=1)
    Label(root, text='Password', font=('ariel', 15,),bg='white' ).grid(row=9, column=0)
    pwd = Entry(root, width=30)
    pwd.grid(row=9, column=1)
    Button(root, width=6, bg='green', fg='white', text='Enter', font=('ariel', 15,), command=check).grid(row=10, column=1)
    Button(root, width=6, bg='red', fg='white', text='Close', font=('ariel', 15,), command=root.destroy).grid(row=11,column=1)

    root.mainloop()


def check():

    global un, pwd, login, root
    u = un.get()
    p = pwd.get()
    l.execute("select * from librarian")
    flag=0
    for i in l:
        if i[1] == u and i[2] == p:
            flag=1
            root.destroy()
            open_win()
    login.commit()
    if(flag==0):
        messagebox.showinfo("ERROR", "Wrong Username or password \n Plese try again!")


again()