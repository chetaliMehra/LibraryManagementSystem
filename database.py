import sqlite3



#Creating the table which contains the books
# c=sqlite3.connect("Library.db")
# d=c.cursor()
#d.execute("CREATE TABLE IF NOT EXISTS book(ISBN char(13) NOT NULL, Title varchar(80) NOT NULL, Author varchar(80) NOT NULL, Category varchar(80) NOT NULL,Price int(4) NOT NULL,Copies int(10) NOT NULL)")

#d.execute("INSERT INTO book VALUES ('9788654552277', 'X-Men: God Loves, Man Kills', 'Chris', 'Comics', 98, 39),('0964161484100', 'Mike Tyson : Undisputed Truth', 'Larry Sloman, Mike Tyson', 'Sports', 654, 79),('6901142585540', 'V for Vendetta', 'Alan Moore', 'Comics', 600, 23),('9094996245442', 'When Breath Becomes Air', 'Paul Kalanithi', 'Medical', 500, 94), ('8653491200700', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 432, 120)")
#c.commit()


#View the book table
# d.execute("select * from book")
# vf=d.fetchall()
# for i in vf:
#     print(i)

#Creating a table which will the username and password of the libarian
# login=sqlite3.connect("admin.db")
# l=login.cursor()

# l.execute("CREATE TABLE IF NOT EXISTS librarian (id int(11) NOT NULL, username varchar(20) NOT NULL, password char(40) NOT NULL)")
#creating a table for issued books
# c=sqlite3.connect("Library.db")
# d=c.cursor()
# d.execute("CREATE TABLE IF NOT EXISTS book_issue (issue_id int(11) NOT NULL, member varchar(20) NOT NULL, book_isbn varchar(13) NOT NULL, issue_date DATE NOT NULL,due_date DATE NOT NULL,Return_status varchar(4) NOT NULL)")
# d.execute("INSERT INTO book_issue VALUES (01201, 'Shrikant Sharma','9788654552277', '2023-06-25',2023-07-25, 'NO'),(25631,'Mohan Tyagi','9788654552277','2023-06-29','2023-07-29','NO'),(78541,'Ramlal shah','9788654552277','2023-07-11','2023-08-11','NO')")
#
# c.commit()

# Viewing table book_issue:
# d.execute("select * from book_issue")
# vf=d.fetchall()
# for i in vf:
#     print(i)

#creating a table that stores the details of the all the members of the library
# c=sqlite3.connect("admin.db")
# d=c.cursor()
# d.execute("CREATE TABLE IF NOT EXISTS member_details(Member_id int,Name text, Contact int, Address text, Joining_date DATE  ) ")
#
# d.execute("INSERT INTO member_details VALUES (001,'Shrikant Sharma',9125634875, 'Shanti vihar, Rudrapur','2022-12-25' ),(002,'Mohan Tyagi',9125658460, 'Alliance, Rudrapur','2022-12-25' ),(002,'Ramlal shah',9125658460, 'Malik Colony, Rudrapur','2022-12-25' )")
#c.commit()

# d.execute("select * from member_details")
# vf=d.fetchall()
# for i in vf:
#     print(i)

# login=sqlite3.connect("admin.db")
# l=login.cursor()
#
# l.execute("CREATE TABLE IF NOT EXISTS librarian (id int(11) NOT NULL, username varchar(20) NOT NULL, password char(40) NOT NULL)")
# l.execute("INSERT INTO librarian values(1,'Vani',hellohello23)")