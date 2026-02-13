from customtkinter import *
from PIL import Image
from tkinter import messagebox, ttk
import database 
        # FUNTIONS

def delete_all_employees():
    result= messagebox.askyesno("Confirm", "Are you sure you want to delete all employees?")
    if result:
        database.deleteall_records()
    else:
        pass



def show_all_employees():
    treeview_data()
    searchEntry.delete(0, END)
    searchBox.set("Search by")



def search_employee():
    if searchEntry.get() == "":
        messagebox.showerror("Error", "Please enter a search term")
    elif searchBox.get() == "Search by":
        messagebox.showerror("Error", "Please select a search criteria")
    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())  
        for employee in searched_data:
          tree.insert("",END,values=employee)
      




def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select an employee to delete")
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Employee deleted successfully")





def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select an employee to update")
    else:
        database.update(idEntry.get(),nameEntry.get(),roleBox.get(),phoneEntry.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Employee updated successfully")


def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)["values"]
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        roleBox.set(row[2])
        phoneEntry.insert(0, row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])





def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    salaryEntry.delete(0, END)
    roleBox.set('web developer')
    genderBox.set('Male')
    salaryEntry.delete(0, END)





def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert("",END,values=employee)






def add_employee():
    if idEntry.get() == "" or nameEntry.get() == "" or phoneEntry.get() == "" or salaryEntry.get() == "":
        messagebox.showerror("Error", "Please fill in all fields")

    elif database.id_exists(idEntry.get()):
        messagebox.showerror("Error", "Employee ID already exists")
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror("Error", "Employee ID must start with 'EMP'")
    else:
        database.insert(idEntry.get(), nameEntry.get(), roleBox.get(), phoneEntry.get(), genderBox.get(), salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success", "Employee added successfully")












window=CTk()
window.title("Employee Management System")
window.geometry("930x580+100+100")
window.resizable(False, False)
window.configure(fg_color="black")




logo=CTkImage(Image.open("bgpic.png"), size=(950, 165))
logoLabel=CTkLabel(window, image=logo, text="")
logoLabel.grid(row=0, column=0, columnspan=2)

leftFrame=CTkFrame(window, fg_color="black")
leftFrame.grid(row=1, column=0)

idLabel=CTkLabel(leftFrame, text="Employee ID", font=("Arial", 18,"bold"),text_color="white")
idLabel.grid(row=0, column=0,padx=20, pady=20,sticky="w")

idEntry=CTkEntry(leftFrame,font=("Arial", 18, "bold"),width=180)
idEntry.grid(row=0, column=1) 


nameLabel=CTkLabel(leftFrame, text="Employee Name", font=("Arial", 18,"bold"),text_color="white")
nameLabel.grid(row=1, column=0,padx=20, pady=20,sticky="w")

nameEntry=CTkEntry(leftFrame,font=("Arial", 18, "bold"),width=180)
nameEntry.grid(row=1, column=1)

phoneLabel=CTkLabel(leftFrame, text="Employee Phone", font=("Arial", 18,"bold"),text_color="white")
phoneLabel.grid(row=2, column=0,padx=20,pady=20,sticky="w")

phoneEntry=CTkEntry(leftFrame,font=("Arial", 18, "bold"),width=180)
phoneEntry.grid(row=2, column=1)


roleLabel=CTkLabel(leftFrame, text="Employee Role", font=("Arial", 18,"bold"),text_color="white")
roleLabel.grid(row=3, column=0,padx=20, pady=20,sticky="w")

role_options = ["Manager", "Developer", "Designer", "Tester", "HR"]

roleBox=CTkComboBox(leftFrame, values=role_options, font=("Arial", 18, "bold"), width=180,state="readonly")
roleBox.grid(row=3, column=1)
roleBox.set(role_options[0])


genderLabel=CTkLabel(leftFrame, text="Employee Gender", font=("Arial", 18,"bold"),text_color="white")
genderLabel.grid(row=4, column=0,padx=20, pady=20,sticky="w")

gender_options = ["Male", "Female", "Other"]

genderBox=CTkComboBox(leftFrame, values=gender_options, font=("Arial", 18, "bold"), width=180,state="readonly")
genderBox.grid(row=4, column=1)
genderBox.set(gender_options[0])

salaryLabel=CTkLabel(leftFrame, text="Employee Salary", font=("Arial", 18,"bold"),text_color="white")
salaryLabel.grid(row=5, column=0,padx=20, pady=20,sticky="w")

salaryEntry=CTkEntry(leftFrame,font=("Arial", 18, "bold"),width=180)
salaryEntry.grid(row=5, column=1)


rightFrame=CTkFrame(window)
rightFrame.grid(row=1, column=1)

search_options = ["ID", "Name", "Role", "Gender", "Salary"]
searchBox=CTkComboBox(rightFrame, values=search_options, state="readonly")
searchBox.grid(row=0, column=0)
searchBox.set(search_options[0]) 


searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1)

searchButton=CTkButton(rightFrame, text="Search", width=100,command=search_employee)
searchButton.grid(row=0, column=2)

showallButton=CTkButton(rightFrame, text="Show All", width=100,command=show_all_employees)
showallButton.grid(row=0, column=3,pady=10)


tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1, column=0,columnspan=4)

tree["columns"]=("ID", "Name", "Role", "Phone", "Gender", "Salary")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Role", text="Role")
tree.heading("Phone", text="Phone")
tree.heading("Gender", text="Gender")
tree.heading("Salary", text="Salary")   

tree.configure(show="headings")
tree.column("ID", width=100,anchor="center")
tree.column("Name", width=150,anchor="center")
tree.column("Role", width=150,anchor="center")
tree.column("Phone", width=150,anchor="center")
tree.column("Gender", width=100,anchor="center")
tree.column("Salary", width=150,anchor="center")


style=ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 18, "bold"))
style.configure("Treeview", font=("Arial", 14,'bold'),rowheight=30,background="black",foreground="white")


scrollbar=ttk.Scrollbar(rightFrame, orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1, column=4,sticky="ns")

tree.configure(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window,fg_color="black")
buttonFrame.grid(row=2, column=0, columnspan=2,pady=20)

newButton=CTkButton(buttonFrame, text="New Employee" ,font=("Arial", 18, "bold"), width=160,corner_radius=15,command=lambda: clear(True))
newButton.grid(row=0, column=0,pady=5)


addButton=CTkButton(buttonFrame, text="Add Employee" ,font=("Arial", 18, "bold"), width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0, column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame, text="Update Employee" ,font=("Arial", 18, "bold"), width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0, column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame, text="Delete Employee" ,font=("Arial", 18, "bold"), width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0, column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame, text="Delete All" ,font=("Arial", 18, "bold"), width=160,corner_radius=15,command=delete_all_employees)
deleteallButton.grid(row=0, column=4,pady=5,padx=5)



treeview_data()

window.bind('<ButtonRelease-1>',selection)

window.mainloop()