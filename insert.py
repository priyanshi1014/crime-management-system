import tkinter as tk
from tkinter import messagebox
from tkinter import *
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="heer@1807",
    database="project"
)

#functionality of cases 
def insert_case():
    case_number = case_number_entry.get()
    description = description_entry.get()
    status = status_entry.get()
    date_opened = date_opened_entry.get()
    date_closed = date_closed_entry.get()
    officer_id = officer_id_entry.get()
    location_id = location_id_entry.get()
    try:
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO Cases (casenumber, description, status, date_opened, date_closed, officer_id, location_id)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''', (case_number, description, status, date_opened, date_closed, officer_id, location_id))
        conn.commit()
        messagebox.showinfo("Success", "Case details inserted successfully")

    except sqlite3.Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

#functionality of criminals
def insert_criminal():
    name = criminal_name_entry.get()
    age = criminal_age_entry.get()
    gender = criminal_gender_entry.get()
    address = criminal_address_entry.get()
    criminal_history = criminal_history_entry.get()

    try:
        conn = sqlite3.connect('crime_database.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO Criminal (name, age, gender, address, criminal_history)
                          VALUES (?, ?, ?, ?, ?)''', (name, age, gender, address, criminal_history))
        conn.commit()
        messagebox.showinfo("Success", "Criminal details inserted successfully")

    except sqlite3.Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()


#functionality of evidences
def insert_evidence():
    evidence_id = evidence_id_entry.get()
    description = evidence_description_entry.get()
    type = evidence_type_entry.get()
    case_id = evidence_case_id_entry.get()
    

    try:
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO evidences (evidence_id,description, type, case_id)
                          VALUES (?, ?, ?, ?)''', (evidence_id,description, type, case_id))
        conn.commit()
        messagebox.showinfo("Success", "Evidence details inserted successfully")

    except sqlite3.Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()


#functionality of witnesses
def insert_witness():
    witness_id = witness_id_enty.get()
    name = witness_name_entry.get()
    contact_info = witness_contact_info_entry.get()
    statement = witness_statement_entry.get()
    case_id = witness_case_id_entry.get()
    gender = witness_gender_entry.get()
    age = witness_age_entry.get()
    

    try:
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO witness (witness_id,name, contact_info, statement, case_id,gender,age)
                          VALUES (?, ?, ?, ?, ?, ?,?)''', (witness_id, name, contact_info, statement, case_id, gender, age))
        conn.commit()
        messagebox.showinfo("Success", "Witness details inserted successfully")

    except sqlite3.Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()



#functionality of location
def insert_location():
    location_id = location_id_entry.get()
    address = location_address_entry.get()
    city = location_city_entry.get()
    state = location_state_entry.get()

    try:
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO location (location_id, address, city, state)
                          VALUES (?, ?, ?, ?)''', (location_id, address, city, state))
        conn.commit()
        messagebox.showinfo("Success", "Location details inserted successfully")

    except sqlite3.Error as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()




insert = tk.Tk()
insert.title("CRIME BRANCH MANAGEMENT SYSTEM")
insert.state('zoomed')

frame = Frame(insert, bg="black")
frame.pack(fill=Y)

bgimage = PhotoImage(file="bg5.png")
Label(frame, image=bgimage).pack()




case_id_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
case_id_entry.place(x=193, y=55)

case_number_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
case_number_entry.place(x=193, y=90)

description_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
description_entry.place(x=193, y=128)

status_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
status_entry.place(x=193, y=165)

date_opened_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
date_opened_entry.place(x=193, y=204)

date_closed_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
date_closed_entry.place(x=193, y=240)

officer_id_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
officer_id_entry.place(x=193, y=276)

location_id_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
location_id_entry.place(x=193, y=315)

icase = Button(insert,text='Insert' ,font=('Times new roman' ,13, 'bold'),fg= 'white',bg='coral',bd=0,width=11, command=insert_case)
icase.place(x=170, y=350)




criminal_id_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
criminal_id_entry.place(x=650, y=48)

criminal_name_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
criminal_name_entry.place(x=650, y=85)

criminal_age_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
criminal_age_entry.place(x=650, y=122)

criminal_gender_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
criminal_gender_entry.place(x=650, y=158)

criminal_address_entry= Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
criminal_address_entry.place(x=650, y=195)

criminal_history_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
criminal_history_entry.place(x=650, y=233)

icriminal = Button(insert,text='Insert' ,font=('Times new roman' ,13, 'bold'),fg= 'white',bg='coral',bd=0,width=11, command=insert_criminal)
icriminal.place(x=620, y=350)





witness_id_enty = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
witness_id_enty.place(x=1080, y=48)

witness_name_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
witness_name_entry.place(x=1080, y=85)

witness_contact_info_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
witness_contact_info_entry.place(x=1080, y=122)

witness_statement_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
witness_statement_entry.place(x=1080, y=158)

witness_case_id_entry= Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
witness_case_id_entry.place(x=1080, y=195)

witness_gender_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
witness_gender_entry.place(x=1080, y=233)

witness_age_entry= Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
witness_age_entry.place(x=1080, y=275)

iwitness = Button(insert,text='Insert' ,font=('Times new roman' ,13, 'bold'),fg= 'white',bg='coral',bd=0,width=11, command=insert_witness)
iwitness.place(x=1050, y=350)





location_id_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
location_id_entry.place(x=460, y=462)

location_address_entry= Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
location_address_entry.place(x=460, y=500)

location_city_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
location_city_entry.place(x=460, y=538)

location_state_entry= Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
location_state_entry.place(x=460, y=575)

ilocation = Button(insert,text='Insert' ,font=('Times new roman' ,13, 'bold'),fg= 'white',bg='coral',bd=0,width=11, command=insert_location)
ilocation.place(x=410, y=650)







evidence_id_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
evidence_id_entry.place(x=910, y=466)

evidence_description_entry= Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
evidence_description_entry.place(x=910, y=504)

evidence_type_entry = Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
evidence_type_entry.place(x=910, y=540)

evidence_case_id_entry= Entry(insert, width=27, font=('Times new roman', 11), bd=0, bg='black', fg='white')
evidence_case_id_entry.place(x=910, y=577)

ilocation = Button(insert,text='Insert' ,font=('Times new roman' ,13, 'bold'),fg= 'white',bg='coral',bd=0,width=11, command=insert_location)
ilocation.place(x=880, y=650)




insert.mainloop()
