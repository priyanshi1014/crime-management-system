import tkinter as tk
from tkinter import messagebox
from tkinter import *
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Function to delete record from the table
def delete_record(table_name, record_id):
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE id = %s", (record_id,))
        conn.commit()
        messagebox.showinfo("Success", f"Record with ID {record_id} deleted successfully from {table_name}")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()

# Function to handle button click event
def delete_record_click():
    table_name = table_name_entry.get()
    record_id = record_id_entry.get()

    if not table_name or not record_id:
        messagebox.showerror("Error", "Please enter both table name and record ID")
        return

    delete_record(table_name, record_id)

    
delete = Tk()
delete.title("CRIME BRANCH MANAGEMENT SYSTEM")
delete.state('zoomed')

frame = Frame(delete, bg="black")
frame.pack(fill=Y)

bgimage = PhotoImage(file="bg6.png")
Label(frame, image=bgimage).pack()


table_name_entry = Entry(delete, width=27, font=('Times new roman', 15), bd=0, bg='black', fg='white')
table_name_entry.place(x=633, y=178)

record_id_entry = Entry(delete, width=27, font=('Times new roman', 15), bd=0, bg='black', fg='white')
record_id_entry.place(x=633, y=265)

delete_button = Button(delete,text='Delete' ,font=('Times new roman' ,16, 'bold'),fg= 'white',bg='coral',bd=0,width=11,command=delete_record_clicks)
delete_button.place(x=633, y=470)


delete.mainloop()
