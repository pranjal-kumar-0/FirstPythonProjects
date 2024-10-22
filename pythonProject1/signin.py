from tkinter import *
from PIL import ImageTk


#Fuctions

def user_enter(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, END)


def password_enter(event):
    if password_entry.get() == 'Password':
        password_entry.delete(0, END)


#GUI
login_window = Tk()
login_window.resizable(0, 0)  #This removes the maximize button, passing false for both values
login_window.title("Login Page")
bg_image = ImageTk.PhotoImage(file='images/bg.jpg')

bgLabel = Label(login_window, image=bg_image)
bgLabel.grid(row=0, column=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'),
                bg='white', fg='firebrick')
heading.place(x=605, y=120)

username_entry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                       borderwidth=0, fg='firebrick')
username_entry.place(x=580, y=200)
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', user_enter)
Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=222)

password_entry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                       borderwidth=0, fg='firebrick')
password_entry.place(x=580, y=260)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', password_enter)  #FocusIn means if we click on it, the fn will run.
Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=282)

print("Hi")
login_window.mainloop()
