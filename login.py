from customtkinter import *

from PIL import Image
from tkinter import messagebox
# login.py
from flask import Flask
app = Flask(__name__)

def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "Please fill in all fields")
    elif usernameEntry.get() == "admin" and passwordEntry.get() == "admin":
        messagebox.showinfo("Success", "Login successful")
        root.destroy()
        import ems
    else: messagebox.showerror("Error", "Invalid username or password")                            

set_appearance_mode("System")
set_default_color_theme("blue")


root=CTk()

root.geometry("930x478")
root.minsize(930,478)
root.maxsize(930,478)

root.title('login page')


image= CTkImage(Image.open("ems.png"), size=(930, 478))
imageLabel=CTkLabel(root, image=image,text="") 
imageLabel.place(x=0, y=0)
headingLabel=CTkLabel(root, text="Employee Management System", bg_color="white", font= ("Arial", 20, "bold"),text_color="black")
headingLabel.place(x=20, y=100)

usernameEntry=CTkEntry(root, placeholder_text="Enter Your Username", width=180)
usernameEntry.place(x=50, y=150)

passwordEntry=CTkEntry(root, placeholder_text="Enter Your Password", width=180 , show="*" ,)
passwordEntry.place(x=50, y=200)

loginButton=CTkButton(root, text="Login" ,cursor="hand2", command=login)
loginButton.place(x=70, y=250)

root.mainloop()
if __name__ == "__main__":
    app.run(debug=True)