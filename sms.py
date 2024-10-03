from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas


def iexit():
    result=messagebox.askyesno("Confirm","Do you want to exit?")
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension=".csv")
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content["values"]
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=["Id","Name","Email","Program","Sign In","Sign Out","ItemTaken","Added Date","Added Time"])
    table.to_csv(url,index=False)
    messagebox.showinfo("Success","Data is saved successfully")



def toplevel_data(title,button_text,command):
    global idEntry, nameEntry, emailEntry, programEntry, SignInEntry, SignOutEntry, ItemTakenEntry, screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)

    idLabel = Label(screen, text="id", font=("times new roman", 20, "bold"))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=("roman", 15, "bold"), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text="Name", font=("times new roman", 20, "bold"))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=("roman", 15, "bold"), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    emailLabel = Label(screen, text="Email", font=("times new roman", 20, "bold"))
    emailLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen, font=("roman", 15, "bold"), width=24)
    emailEntry.grid(row=2, column=1, pady=15, padx=10)

    programLabel = Label(screen, text="Program", font=("times new roman", 20, "bold"))
    programLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    programEntry = Entry(screen, font=("roman", 15, "bold"), width=24)
    programEntry.grid(row=3, column=1, pady=15, padx=10)

    SignInLabel = Label(screen, text="Sign In", font=("times new roman", 20, "bold"))
    SignInLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    SignInEntry = Entry(screen, font=("roman", 15, "bold"), width=24)
    SignInEntry.grid(row=4, column=1, pady=15, padx=10)

    SignOutLabel = Label(screen, text="Sign Out", font=("times new roman", 20, "bold"))
    SignOutLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    SignOutEntry = Entry(screen, font=("roman", 15, "bold"), width=24)
    SignOutEntry.grid(row=5, column=1, pady=15, padx=10)

    ItemTakenLabel = Label(screen, text="Item Taken", font=("times new roman", 20, "bold"))
    ItemTakenLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    ItemTakenEntry = Entry(screen, font=("roman", 15, "bold"), width=24)
    ItemTakenEntry.grid(row=6, column=1, pady=15, padx=10)

    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=7, columnspan=2, pady=15)

    if title == "Update Student":
        indexing = studentTable.focus()
        if not indexing:
            messagebox.showerror("Error", "Please select a student to update.")
            screen.destroy()  
            return
        content = studentTable.item(indexing)
        listdata = content["values"]

        if listdata: 
            idEntry.insert(0, listdata[0])
            nameEntry.insert(0, listdata[1])
            emailEntry.insert(0, listdata[2])
            programEntry.insert(0, listdata[3])
            SignInEntry.insert(0, listdata[4])
            SignOutEntry.insert(0, listdata[5])
            ItemTakenEntry.insert(0, listdata[6])





def update_data():
    query="update student set name=%s,email=%s,program=%s,Sign In=%s,Sign Out=%s,ItemTaken=%s,date=%s,time=%s where id=%s"
    mycursor.execute(query,(nameEntry.get(),emailEntry.get(),programEntry.get(),SignInEntry.get()
                            ,SignOutEntry.get(),ItemTakenEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo("Success",f"Id {idEntry.get()} is modified successfully",parent=screen)
    screen.destroy()
    show_student()






def show_student():
    query = "select * from student"
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert("", END, values=data)



def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content["values"][0]
    query="delete from student where id=%s"
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo("Deleted",f"Id {content_id} is deleted succesfully")
    query="select * from student"
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert("",END,values=data)


def search_data():
    query="select * from student where id=%s or name=%s or email=%s or program=%s or Sign In=%s or Sign Out=%s or ItemTaken=%s"
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),programEntry.get(),SignInEntry.get()
                            ,SignOutEntry.get(),ItemTakenEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert("",END,values=data)





def add_data():
    if idEntry.get() == "" or nameEntry.get() == "" or emailEntry.get() == "" or programEntry.get() == "" or SignInEntry.get() == "" or SignOutEntry.get() == "" or ItemTakenEntry.get() == "":
        messagebox.showerror("Error", "All Fields are required", parent=screen)

    else:
        try:
            query = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query, (
            idEntry.get(), nameEntry.get(), emailEntry.get(), programEntry.get(), SignInEntry.get(),
            SignOutEntry.get(), ItemTakenEntry.get(), date, currenttime))
            con.commit()
            result = messagebox.askyesno("Confirm", "Data added successfully. Do you want to clean the form?",
                                         parent=screen)
            if result:
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                emailEntry.delete(0, END)
                programEntry.delete(0, END)
                SignInEntry.delete(0, END)
                SignOutEntry.delete(0, END)
                ItemTakenEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror("Error", "Id cannot be repeated", parent=screen)
            return

        query="select *from student"
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert("",END,values=data)





def connect():
    global connectWindow, mycursor, con 
    try:
        con = pymysql.connect(host=hostEntry.get(), user=usernameEntry.get(), password=passwordEntry.get())
        mycursor = con.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS studentmanagementsystem")
        mycursor.execute("USE studentmanagementsystem")
        mycursor.execute("""CREATE TABLE IF NOT EXISTS student (
                            id INT NOT NULL PRIMARY KEY,
                            name VARCHAR(30),
                            email VARCHAR(30),
                            program VARCHAR(30),
                            `Sign In` VARCHAR(100),
                            `Sign Out` VARCHAR(20),
                            `Item Taken` VARCHAR(20),
                            date VARCHAR(50),
                            time VARCHAR(50))""")
        messagebox.showinfo("Success", "Database and Table Creation Successful")

        connectWindow.destroy() 

        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL) 
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")




# Functionality Part
def connect_database():
    global hostEntry, usernameEntry, passwordEntry, connectWindow 
    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry("470x250+730+230")
    connectWindow.title("Database Connection")
    connectWindow.resizable(0, 0)

    hostnameLabel = Label(connectWindow, text="Host Name", font=("arial", 20, "bold"))
    hostnameLabel.grid(row=0, column=0, padx=20)

    hostEntry = Entry(connectWindow, font=("roman", 15, "bold"), bd=2)
    hostEntry.grid(row=0, column=1, padx=40, pady=20)

    usernameLabel = Label(connectWindow, text="User Name", font=("arial", 20, "bold"))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=("roman", 15, "bold"), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text="Password", font=("arial", 20, "bold"))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=("roman", 15, "bold"), bd=2, show="*")
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = ttk.Button(connectWindow, text="CONNECT", command=connect)
    connectButton.grid(row=3, columnspan=2, pady=10)


# Slider Function
count = 0
text = ""


def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ""
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)


# Clock Function
def clock():
    global date,currenttime
    date = time.strftime("%d/%m/%Y")
    currenttime = time.strftime("%H:%M:%S")
    datetimeLabel.config(text=f"    Date: {date}\nTime: {currenttime}")
    datetimeLabel.after(1000, clock)


# GUI Part
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme("equilux")
root.geometry("1174x680+0+0")
root.resizable(0, 0)
root.title("Student Management System")

datetimeLabel = Label(root, font=("times new roman", 18, "bold"))
datetimeLabel.place(x=5, y=5)
clock()
s = "Student Management System"
sliderLabel = Label(root, font=("arial", 28, "italic bold"), width=30)
sliderLabel.place(x=210, y=0)
slider()

connectButton = ttk.Button(root, text="Connect database", command=connect_database)
connectButton.place(x=1050, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image = PhotoImage(file="student-avatar.png")
logo_Label = Label(leftFrame, image=logo_image)
logo_Label.grid(row=0, column=0)

addstudentButton = ttk.Button(leftFrame, text="Add Student", width=25, state=DISABLED,command=lambda :toplevel_data("Add Student","Add",add_data))
addstudentButton.grid(row=1, column=0, pady=20)

searchstudentButton = ttk.Button(leftFrame, text="Search Student", width=25, state=DISABLED,command=lambda :toplevel_data("Search Student","Search",search_data))
searchstudentButton.grid(row=2, column=0, pady=20)

deletestudentButton = ttk.Button(leftFrame, text="Delete Student", width=25, state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3, column=0, pady=20)

updatestudentButton = ttk.Button(leftFrame, text="Update Student", width=25, state=DISABLED,command=lambda :toplevel_data("Update Student","Update",update_data))
updatestudentButton.grid(row=4, column=0, pady=20)

showstudentButton = ttk.Button(leftFrame, text="Show Student", width=25, state=DISABLED,command=show_student)
showstudentButton.grid(row=5, column=0, pady=20)

exportstudentButton = ttk.Button(leftFrame, text="Export data", width=25, state=DISABLED,command=export_data)
exportstudentButton.grid(row=6, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text="Exit", width=25, command=iexit)
exitButton.grid(row=7, column=0, pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=("Id", "Name", "Email", "Program", "Sign In", "Sign Out",
                                                 "Item Taken", "Added Date", "Added Time"),
                            xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill=BOTH, expand=1)

studentTable.heading("Id", text="Id")
studentTable.heading("Name", text="Name")
studentTable.heading("Email", text="Email")
studentTable.heading("Program", text="Program")
studentTable.heading("Sign In", text="Sign In")
studentTable.heading("Sign Out", text="Sign Out")
studentTable.heading("Item Taken", text="Item Taken")
studentTable.heading("Added Date", text="Added Date")
studentTable.heading("Added Time", text="Added Time")

studentTable.column("Id",width=50,anchor=CENTER)
studentTable.column("Name",width=300,anchor=CENTER)
studentTable.column("Email",width=300,anchor=CENTER)
studentTable.column("Program",width=200,anchor=CENTER)
studentTable.column("Sign In",width=300,anchor=CENTER)
studentTable.column("Sign Out",width=100,anchor=CENTER)
studentTable.column("Item Taken",width=200,anchor=CENTER)
studentTable.column("Added Date",width=200,anchor=CENTER)
studentTable.column("Added Time",width=200,anchor=CENTER)

style=ttk.Style()

style.configure("Treeview",height=40,font=("arial",12,"bold"),background="black",fieldbackground="grey4")
style.configure("Treeview.Heading",font=("arial",14,"bold"))

studentTable.config(show="headings")

root.mainloop()
