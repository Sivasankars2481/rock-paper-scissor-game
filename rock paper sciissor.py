from tkinter import *
import random


play = Tk()
play .geometry('700x500')
play.title('Rock-Paper-Scissor')
play.configure(bg='lightblue')
choices = {'0':'Rock','1':'Paper','2':'Scissor'}






flag = False
count = 0

def start(flag):
    global count;
    if(flag == 1):
        count+=1
        l4.config(text=count)




def rock():
    computerselected = choices[str(random.randint(0,2))]
    if computerselected == 'Rock':
        result = 'Tie'

    elif computerselected == 'Paper':
        result = 'Computer Wins'

        

    else:
        result = 'Player Wins'
        flag = True
        start(flag)
        




    l1.config(text='Rock')
    l2.config(text=computerselected)
    l3.config(text=result)
   



    disable()

def paper():
    computerselected = choices[str(random.randint(0,2))]
    if computerselected == 'Paper':
        result = 'Tie'
    elif computerselected == 'Scissor':
        result = 'Computer Wins'
    else:
        result = 'Player Wins'
        flag = True
        start(flag)

    l1.config(text='Paper')
    l2.config(text=computerselected)
    l3.config(text=result)
    disable()


def Scissor():
    computerselected = choices[str(random.randint(0,2))]
    if computerselected == 'Scissor':
        result = 'Tie'
    elif computerselected == 'Rock':
        result = 'Computer Wins'

    else:
        result = 'Player Wins'
        flag = True
        start(flag)

    l1.config(text='Scissor')
    l2.config(text=computerselected)
    l3.config(text=result)
    disable()
def disable():
    b1['state'] = 'disable'
    b2['state'] = 'disable'
    b3['state'] = 'disable'
def reset():
    b1['state'] = 'active'
    b2['state'] = 'active'
    b3['state'] = 'active'
    l1.config(text='')
    l2.config(text='')
    l3.config(text='')







Label(play,text='Rock-Paper-Scissor',font=('calibri',20),bg='white').place(x=200,y=30)
Label(play,text='Choose Anyone',font=('calibri',18),fg='green',bg='lightblue').place(x=230,y=80)

b1 = Button(play,text='Rock',font=('calibri',18),bg='blue',fg='white',width=10,height=1,command=rock)
b1.place(x=50,y=140)
b2 = Button(play,text='Paper',font=('calibri',18),bg='blue',fg='white',width=10,height=1,command=paper)
b2.place(x=250,y=140)
b3 = Button(play,text='Scissor',font=('calibri',18),bg='blue',fg='white',width=10,height=1,command=Scissor)
b3.place(x=450,y=140)

f1 = Frame(play, width='580',height='150')
f1.place(x=50,y=250)

Label(f1, text='Player Selected : ',font=('calibri',18,'bold')).place(x=20,y=10)
Label(f1, text='Computer Selected : ',font=('calibri',18,'bold')).place(x=330,y=10)

l1= Label(f1,font=('calibri',20,'bold'),fg='red')
l1.place(x=60,y=40)

l2= Label(f1,font=('calibri',20,'bold'),fg='blue')
l2.place(x=370,y=40)

l3 = Label(play,font=('calibri',25,'bold'),fg='red',relief='solid')
l3.place(x=50,y=400)

b4= Button(play,text='Reset',font=('calibri',20),bg='red',fg='white',width='10',height='1',command=reset)
b4.place(x=400,y=400)

l4 = Label(play,text='Player Score:',font=('calibri',25),bg='light blue',fg='black')
l4.place(x=80,y=450)
l4 = Label(play,font=('calibri',25,'bold'),bg='white')
l4.place(x=260,y=450)


play.mainloop()