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

def save_to_notepad():
    with open("case_details.txt", "w") as file:
        file.write(txt_result.get("1.0", "end-1c"))
    messagebox.showinfo("Success", "Case details saved to 'case_details.txt'")

def fetch_details():
    case_id = caseid.get()
    criminal_name = criminal.get()
    crime = crime_as.get()

    if not case_id or not criminal_name or not crime:
        messagebox.showerror("Error", "Please enter all details")
        return

    try:
        conn = sqlite3.connect('crime_database.db')
        cursor = conn.cursor()

        # Retrieve case details
        cursor.execute("SELECT * FROM Cases WHERE case_id=?", (case_id,))
        case_data = cursor.fetchone()

        if case_data:
            case_details = f"Case ID: {case_data[0]}\nCase Number: {case_data[1]}\nDescription: {case_data[2]}\nStatus: {case_data[3]}\nDate Opened: {case_data[4]}\nDate Closed: {case_data[5]}\nOfficer ID: {case_data[6]}\nLocation ID: {case_data[7]}\n\n"

            # Retrieve criminal details
            cursor.execute("SELECT * FROM Suspects WHERE case_id=?", (case_id,))
            criminal_data = cursor.fetchall()
            criminal_details = "Criminal Details:\n"
            for criminal in criminal_data:
                criminal_details += f"Suspect ID: {criminal[0]}, Name: {criminal[1]}, Criminal Activities: {criminal[2]}, Status: {criminal[3]}, Age: {criminal[5]}, Gender: {criminal[6]}\n"

            # Retrieve witness details
            cursor.execute("SELECT * FROM witness WHERE case_id=?", (case_id,))
            witness_data = cursor.fetchall()
            witness_details = "Witness Details:\n"
            for witness in witness_data:
                witness_details += f"Witness ID: {witness[0]}, Name: {witness[1]}, Contact Info: {witness[2]}, Statement: {witness[3]}, Age: {witness[5]}, Gender: {witness[6]}\n"

            # Retrieve evidence details
            cursor.execute("SELECT * FROM evidences WHERE case_id=?", (case_id,))
            evidence_data = cursor.fetchall()
            evidence_details = "Evidence Details:\n"
            for evidence in evidence_data:
                evidence_details += f"Evidence ID: {evidence[0]}, Description: {evidence[1]}, Type: {evidence[2]}\n"

            # Retrieve location details
            cursor.execute("SELECT * FROM location WHERE location_id=?", (case_data[7],))
            location_data = cursor.fetchone()
            location_details = f"Location Details:\nLocation ID: {location_data[0]}, Address: {location_data[1]}, City: {location_data[2]}, State: {location_data[3]}"

            # Display details in scrolled text
            txt_result.delete(1.0, END)
            txt_result.insert(END, case_details + criminal_details + witness_details + evidence_details + location_details)
        else:
            messagebox.showerror("Error", "Case ID not found")

        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()


view = Tk()
view.title("CRIME BRANCH MANAGEMENT SYSTEM")
view.state('zoomed')

frame = Frame(view, bg="black")
frame.pack(fill=Y)

bgimage = PhotoImage(file="bg4.png")
Label(frame, image=bgimage).pack()

caseid = Entry(view, width=27, font=('Times new roman', 15), bd=0, bg='black', fg='white')
caseid.place(x=250, y=192)

criminal = Entry(view, width=27, font=('Times new roman', 15), bd=0, bg='black', fg='white')
criminal.place(x=250, y=251)

crime_as = Entry(view, width=27, font=('Times new roman', 15), bd=0, bg='black', fg='white')
crime_as.place(x=250, y=318)


btn_fetch = Button(view, text='Fetch Details' ,font=('Times new roman' ,16, 'bold'),fg= 'white',bg='coral',bd=0,width=11, command=fetch_details)
btn_fetch.place(x=300, y=440)

btn_save = Button(view,text='Login' ,font=('Times new roman' ,16, 'bold'),fg= 'white',bg='coral',bd=0,width=11, command=save_to_notepad)
btn_save.place(x=300, y=575)

txt_result = scrolledtext.ScrolledText(view, width=65, height=29, font=('Times new roman', 12),bg='black',fg='white')
txt_result.place(x=775, y=130)

view.mainloop()



