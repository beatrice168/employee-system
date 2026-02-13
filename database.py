import pymysql
from tkinter import messagebox

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_database():

    global mycursor,conn
    try:
    
         conn=pymysql.connect(host='localhost', user='root', password='12345678')
         mycursor=conn.cursor()

    except:
        messagebox.showerror("Error", "Error connecting to the database")
        return
    
    mycursor.execute("CREATE DATABASE IF NOT EXISTS employee_data")
    mycursor.execute("USE employee_data")
    mycursor.execute("CREATE TABLE IF NOT EXISTS data(id VARCHAR(30), name VARCHAR(50), role VARCHAR(50), phone VARCHAR(15), gender VARCHAR(15), salary DECIMAL(10,2))")




def insert(id, name, role,phone,gender,salary): 
    mycursor.execute('INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s)', (id, name, role, phone, gender, salary))
    conn.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id = %s',id)
    result=mycursor.fetchone()
    return result[0] > 0


def fetch_employees():
    mycursor.execute('SELECT * from data')
    result = mycursor.fetchall()
    return result

def update(id,new_name,new_role,new_phone,new_gender,new_salary):
    mycursor.execute('UPDATE data SET name=%s, role=%s, phone=%s, gender=%s, salary=%s WHERE id=%s',(new_name,new_role,new_phone,new_gender,new_salary,id))
    conn.commit()


def delete(id):
    mycursor.execute('DELETE FROM data WHERE id=%s',(id))
    conn.commit()

def search(option, value):
   mycursor.execute(
    f"SELECT * FROM data WHERE {option} LIKE %s",
    ('%' + value + '%',)
     )   
   result=mycursor.fetchall()
   return result

def delete_all_records():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()




connect_database()