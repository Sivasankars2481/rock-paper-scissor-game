from tkinter import *
import tkinter.messagebox
import mysql.connector

db= mysql.connector.connect(host = 'localhost',user='root',password='',db='login')
cursor = db.cursor()


def admin():
    global admin_frame,admin_username,admin_password
    admin_frame = Frame(homepage,width=350,height=200)
    admin_frame.place(x=50,y=130)
    Label(admin_frame,text='UserName',font=('calibri',15)).place(x=30,y=30)
    Label(admin_frame, text='Password', font=('calibri', 15)).place(x=30, y=80)
    admin_username = StringVar()
    admin_password = StringVar()
    Entry(admin_frame,textvariable=admin_username,font=('calibri',13),bg = 'lightgreen',
          ).place(x=140,y=30)
    Entry(admin_frame, textvariable=admin_password, font=('calibri', 13), bg='lightgreen',
         ).place(x=140, y=80)
    Button(admin_frame,text='Login',font=('calibri',13),bg='green',
           width='8',height='1',fg='white').place(x=230,y=130)



def user():
    global user_frame,user_username,user_password
    user_frame = Frame(homepage,width=350,height=200)
    user_frame.place(x=450,y=130)
    Label(user_frame,text='UserName',font=('calibri',15)).place(x=30,y=30)
    Label(user_frame, text='Password', font=('calibri', 15)).place(x=30, y=80)
    user_username = StringVar()
    user_password = StringVar()
    Entry(user_frame,textvariable=user_username,font=('calibri',13),bg = 'lightgreen',
          ).place(x=140,y=30)
    Entry(user_frame, textvariable=user_password, font=('calibri', 13), bg='lightgreen',
         ).place(x=140, y=80)
    Button(user_frame,text='Login',font=('calibri',13),bg='green',
           width='8',height='1',fg='white',command=user_login).place(x=230,y=130)
    Button(user_frame, text='Signup', font=('calibri', 13), bg='green',
           width='8', height='1', fg='white',command=register).place(x=30, y=130)

def user_login():
    username = user_username.get()
    password = user_password.get()
    cursor.execute('select * from logindetails where Username = %s and password=%s',[username,password])
    data = cursor.fetchone()
    if data!= None:
        tkinter.messagebox.showinfo('Authenticate','Welcome User')
    else:
        tkinter.messagebox.showinfo('Authenticate','Invlaid User')


def register():
    global register_frame,register_username,register_password
    global register_name, register_mail ,register_gender , register_address
    register_frame = Frame(homepage,width=350,height = 450)
    register_frame.place(x=850,y=130)
    Label(register_frame,text='Name',font=('Calibri',15)).place(x=30,y=30)
    Label(register_frame, text='Mail', font=('Calibri', 15)).place(x=30, y=80)
    Label(register_frame, text='Gender', font=('Calibri', 15)).place(x=30, y=130)
    Label(register_frame, text='Address', font=('Calibri', 15)).place(x=30, y=180)
    Label(register_frame, text='Username', font=('Calibri', 15)).place(x=30, y=230)
    Label(register_frame, text='Password', font=('Calibri', 15)).place(x=30, y=280)
    register_name = StringVar()
    register_mail = StringVar()
    register_gender = StringVar()
    register_address = StringVar()
    register_username = StringVar()
    register_password = StringVar()
    Entry(register_frame,textvariable=register_name,font=('calibri',13),
          bg='lightgreen').place(x=140,y=30)
    Entry(register_frame,textvariable=register_mail,font=('calibri',13),
          bg='lightgreen').place(x=140,y=80)
    Radiobutton(register_frame,text='Male',font=('calibri',13),variable= register_gender,
                bg='lightgreen').place(x=140,y=130)
    Radiobutton(register_frame, text='Female', font=('calibri', 13),variable= register_gender,
                bg='lightgreen').place(x=230, y=130)
    Entry(register_frame, textvariable=register_address, font=('calibri', 13),
          bg='lightgreen').place(x=140, y=180)
    Entry(register_frame, textvariable=register_username, font=('calibri', 13),
          bg='lightgreen').place(x=140, y=230)
    Entry(register_frame, textvariable=register_password, font=('calibri', 13),
          bg='lightgreen').place(x=140, y=280)
    Button(register_frame,text='Submit',font=('calibri',13),bg = 'green',
           width='8',height='1',fg='white',command=store_data).place(x=240,y=330)



def store_data():
    name = register_name.get()
    mail = register_mail.get()
    gender = register_gender.get()
    address = register_address.get()
    username = register_username.get()
    password= register_password.get()
    cursor.execute('insert into logindetails(Name,sSmail,gender,address,'
                   'username,password) values(%s,%s,%s,%s,%s,%s)',
                   [name,mail,gender,address,username,password])
    db.commit()
    tkinter.messagebox.showinfo('Authenicate','Registered Sucessfully')




def startpage():
     global homepage
     homepage = Tk()
     homepage.geometry('1300x600')
     homepage.title('Authentication')
     homepage.configure(bg='lightgreen')
     Label(homepage,text='Welcome to login Page',font=('calibri',25)).place(x=500,y=20)
     Button(homepage,text='Admin',font=('calibri',15),bg='green',fg='white',
            width='12',height='1',command=admin).place(x=60,y=80)
     Button(homepage, text='Login', font=('calibri', 15), bg='green', fg='white',
            width='12', height='1',command=user).place(x=1000, y=80)
     homepage.mainloop()


startpage()