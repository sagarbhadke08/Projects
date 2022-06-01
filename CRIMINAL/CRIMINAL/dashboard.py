import cv2
import numpy as np 

import os
from dbConnection import conn
#conn = sqlite3.connect('database.db')

from PIL import ImageTk
from matplotlib import pyplot as plt
from tkinter import filedialog
import PIL.Image, PIL.ImageTk
from tkinter import *
import mysql.connector as con
import tkinter.messagebox
global var
import TrainModule
global screen
from dbConnection import view_all_attendance
def main_screen():
    
    
    global screen3
    screen3=Tk()
    #screen3=Toplevel(screen)
   # var = StringVar()
    C = Canvas(screen3, bg="blue", height=250, width=300)
    
    filename = PhotoImage(file = "images.gif")
    background_label = Label(screen3, image=filename)
    background_label.image=filename
    
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    C.pack()
    screen3.configure(background='white')
    screen3.title("DASHBOARD")
    screen3.geometry('1280x720')
    Label(screen3, text="CRIMNAL IDENTIFICATION SYSTEM", bg="Grey", height=1, width=250,font=("Arial Bold", 20)).pack()
    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()

    Label(screen3, text="", bg="white").pack()
    b1 =  Button(screen3,text="ADD CRIMINAL",height=2,width=30,bg="black",fg="white",font=("Arial Bold", 13))
    
    b1.pack()
    Label(screen3, text="", bg="white").pack()
    b2=Button(screen3,text="TRAIN MODEL",height=2,width=30,bg="black",fg="white",font=("Arial Bold", 13))
    b2.pack()
    Label(screen3, text="", bg="white").pack()
    b3= Button(screen3, text="DETECT CRIMINAL ",height=2,width=30,bg="black",fg="white",font=("Arial Bold", 13), command= oc)
    b3.pack()
   
    
    Label(screen3, text="", bg="white").pack()
    b6 = Button(screen3, text="Exit", height=2, width=30, bg="black", fg="white", font=("Arial Bold", 13),
                command=close)
    b6.pack()
    screen3.mainloop()



def oc():
    import oc
    screen3.destroy()

def close():
    import admin_login
    screen3.destroy()
    






def attend():
    global screen2
    global name1_
    global mobile1_
    global class1_
    global div1_
    global password_
    global email_
    screen2=Toplevel(screen3)
    screen2.configure(background='white')
    screen2.geometry('1280x720')
    Label(screen2, text="CRIMNAL IDENTIFICATION SYSTEM", font=("Arial Bold", 25),bg="grey",width=250,height=2).pack()
    Label(screen2, text="", bg="white").pack()
    Label(screen2, text="", bg="white").pack()
    name = Label(screen2, text="Name", height=2, bg="white",font=("Arial Bold", 11))
    name.pack()
    name1_ = Entry(screen2, width=20)
    name1_.pack()

    email = Label(screen2, text="Email Id", height=2, bg="white",font=("Arial Bold", 11))
    email.pack()
    email_ = Entry(screen2, width=20)
    email_.pack()

    password = Label(screen2, text="Password", height=2, bg="white",font=("Arial Bold", 11))
    password.pack()
    password_ = Entry(screen2, width=20)
    password_.pack()
   
   


    mobile = Label(screen2, text="mobile", height=2, bg="white",font=("Arial Bold", 11))
    mobile.pack()
    mobile1_ = Entry(screen2, width=20)
    mobile1_.pack()

    class_ = Label(screen2, text="Class", height=2, bg="white",font=("Arial Bold", 11))
    class_.pack()
    class1_ = Entry(screen2, width=20)
    class1_.pack()

    
    div_ = Label(screen2, text="Division", height=2, bg="white",font=("Arial Bold", 11))
    div_.pack()
    div1_ = Entry(screen2, width=20)
    div1_.pack()

    Label(screen2, text="", bg="white").pack()
    Label(screen2, text="", bg="white").pack()
    login = Button(screen2, text="Add Record", height=2, width=30,bg="black",fg="white",font=("Arial Bold", 13))
    login.pack()



 
    cv2.destroyAllWindows()



main_screen()







