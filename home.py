from tkinter import *
from tkinter import messagebox

#functionality

def view_open():
    home.destroy()
    import view

def insert_open():
    home.destroy()
    import insert

def delete_open():
    home.destroy()
    import delete

home=Tk()
home.title("CRIME BRANCH MANAGEMENT SYSTEM")
home.state('zoomed')


frame=Frame(home,bg="black")
frame.pack(fill=Y)


bgimage=PhotoImage(file="bg3.png")
Label(frame,image=bgimage).pack()


view=Button(home,text='View case details' ,font=('Times new roman' ,16, 'bold'),fg= 'white',bg='coral',bd=0,width=22,height=2,command=view_open)
view.place(x=150,y=350)


insert=Button(home,text='Insert new Data' ,font=('Times new roman' ,16, 'bold'),fg= 'white',bg='coral',bd=0,width=22,height=2,command=insert_open)
insert.place(x=550,y=350)


delete=Button(home,text='Delete Data' ,font=('Times new roman' ,16, 'bold'),fg= 'white',bg='coral',bd=0,width=22,height=2,command=delete_open)
delete.place(x=950,y=350)








home.mainloop()
