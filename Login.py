import sys
from tkinter import *
from tkinter import messagebox
from functools import partial
import helpers as helpers


# Functions
def validateLogin(username, password):
	""" Receives the username and password entered into the entry fields and tries to login to SQL Server """
	if(helpers.sqlLogin(username.get(), password.get())):
		print("Move To Next Page")
		# Move to next page
	else:
		messagebox.showerror("Login Error", "Your username or password was incorrect, please try again.")
	return

def quit():
    sys.exit()


# GUI
# Window
form = Tk()  
form.geometry('1000x600')  
form.title('Login Form')

# Username label and entry field
usernameLabel = Label(form, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameField = Entry(form, textvariable=username).grid(row=0, column=1)  

# Password label and entry field
passwordLabel = Label(form,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordField = Entry(form, textvariable=password, show='*').grid(row=1, column=1)  

# Login button
validateLogin = partial(validateLogin, username, password)
loginButton = Button(form, text="Login", command=validateLogin).grid(row=4, column=0)  

# Cancel button
cancelButton = Button(form, text="Cancel", command=quit).grid(row=4, column=1)  


# Main Program
form.mainloop()