from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror("Error","Fields cannot be empty")
    elif usernameEntry.get()=="Faizan" and passwordEntry.get()=="1234":
        messagebox.showinfo("Success","Welcome")
        window.destroy()
        import sms

    else:
        messagebox.showerror("Error","Please enter correct credentials")


window=Tk()

window.geometry("1280x700+0+0")
window.title("Login System Of Student Management System")

window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file="background.png")

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg="",bd=0,highlightthickness=0)
loginFrame.place(x=390,y=150)


logoImage=PhotoImage(file="student-with-graduation-cap.png")

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file="user.png")
usernameLabel=Label(loginFrame,image=usernameImage,text="Username",compound=LEFT
                    ,font=("times new roman",20,"bold"),bg="white")
usernameLabel.grid(row=1,column=0,pady=10,padx=10)

usernameEntry=Entry(loginFrame ,font=("times new roman",20,"bold"),bd=5)
usernameEntry.grid(row=1,column=1,pady=10,padx=10)

passwordImage=PhotoImage(file="padlock.png")
passwordLabel=Label(loginFrame,image=passwordImage,text="Password",compound=LEFT
                    ,font=("times new roman",20,"bold"),bg="white")
passwordLabel.grid(row=2,column=0,pady=10,padx=10)

passwordEntry=Entry(loginFrame ,font=("times new roman",20,"bold"),bd=5)
passwordEntry.grid(row=2,column=1,pady=10,padx=10)

loginButton=Button(loginFrame,text="Login",font=("times new roman",14,"bold"),width=15,cursor="hand2",command=login)
loginButton.grid(row=3,column=1,pady=10)


window.mainloop()