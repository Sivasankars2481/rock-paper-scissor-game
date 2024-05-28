import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='',db='details')
cursor = db.cursor()

def add():
    global Pro_Id, Pro_name,
    admin_frame = Frame(homepage, width=350, height=200)
    admin_frame.place(x=50, y=130)
    Label(admin_frame, text='UserName', font=('calibri', 15)).place(x=30, y=30)
    Label(admin_frame, text='Password', font=('calibri', 15)).place(x=30, y=80)
    admin_username = StringVar()
    admin_password = StringVar()
    Entry(admin_frame, textvariable=admin_username, font=('calibri', 13), bg='lightgreen',
          ).place(x=140, y=30)
    Entry(admin_frame, textvariable=admin_password, font=('calibri', 13), bg='lightgreen',
          ).place(x=140, y=80)
    Button(admin_frame, text='Login', font=('calibri', 13), bg='green',
           width='8', height='1', fg='white').place(x=230, y=130)


def start():
    global page
    page = Tk()
    page.geometry('1300x600')
    page.title('Authentication')
    page.configure(bg='lightgreen')
    Label(page, text='Product List', font=('calibri', 25)).place(x=500, y=20)
    Label(page,)
    Button(page, text='Add', font=('calibri', 15), bg='green', fg='white',
           width='12', height='1',).place(x=60, y=80)
    Button(page, text='Update', font=('calibri', 15), bg='green', fg='white',
           width='12', height='1', ).place(x=500, y=80)
    Button(page, text='Delete', font=('calibri', 15), bg='green', fg='white',
           width='12', height='1', ).place(x=1000, y=80)



    page.mainloop()


start()

