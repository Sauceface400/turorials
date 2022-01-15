from tkinter import *
import os

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def Login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("success")
    screen3.geometry("150x100")
    Label(screen3 ,text = "Login success").pack()
    Button(screen3 ,text = "OK", command = delete2).pack()

def Password_not_recognize():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("success")
    screen4.geometry("150x100")
    Label(screen4 ,text = "Password error").pack()
    Button(screen4 ,text = "OK", command = delete3).pack()

def User_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("success")
    screen5.geometry("150x100")
    Label(screen5 ,text = "User not found").pack()
    Button(screen5 ,text = "OK", command = delete4).pack()


def Login_confirm():
    Username1 = username.get()
    Password1 = password_varify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir()
    if Username1 in list_of_files:
        file1 = open(Username1, "r")
        verify = file1.read().splitlines()
        if Password1 in verify:
            Login_success()
        else:
            Password_not_recognize()
    else:
            User_not_found()     

#this for the register button
def Register_user():
    print("working")

    username_details = Username.get()
    Password_details = Password.get()

    file = open(username_details, "w")
    file.write(username_details+"\n")#this is so that the text wont be in the same line
    file.write(Password_details)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration is successful").pack()

#this is for to take you into the registarion page
def registration():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("registration")
    screen1.geometry("300x250")

    global Username
    global Password
    global username_entry
    global password_entry
    Username = StringVar()
    Password = StringVar()

    Label(screen1, text = "Plase enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Create your username: ").pack()
    username_entry = Entry(screen1, textvariable = Username)
    username_entry.pack()
    Label(screen1, text = "Create your password: ").pack()
    password_entry = Entry(screen1, textvariable = Password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 15, height = 1, command = Register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login page")
    screen2.geometry("300x300")
    Label(screen2, text = "Please enter your login and password").pack()
    Label(screen2, text = "").pack()

    global username
    global password_varify

    username = StringVar()
    password_varify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text = "Username").pack()
    username_entry1 = Entry(screen2, textvariable = username)
    username_entry1.pack()
    Label(screen2,text = "").pack()
    Label(screen2, text = "Password").pack()
    password_entry1 = Entry(screen2, textvariable = password_varify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = Login_confirm).pack()



#This is the making of a screen
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    Label(text = "Notes 1.0", bg = "grey", width = 30,font = ("Caliber",13)).pack()
    Label(text = " ").pack()
    Button(text = "Login",height = 2,width = 30, command = login).pack()
    Label(text = " ").pack()
    Button(text = "Registration",height = 2,width = 250, command = registration).pack()
    screen.mainloop()
main_screen()