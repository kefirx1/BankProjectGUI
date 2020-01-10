import time, os, sys
import pymysql as p
from tkinter import *

def authentication(master, loginE, passwordE, l1):
    #Create empty tuple
    temp = ()
    #Connect with data base
    try:
        myBase=p.connect(host="localhost", user="root", db="bank")
    except:
        print("Nie udało się połączyć z bazą danych")
        time.sleep(2)
        sys.exit()
    cursor = myBase.cursor()

    #Authentication
    cursor.execute("SELECT login FROM data WHERE login in ('{}')".format(loginE.get()))
    loginB=cursor.fetchall()
    if loginB !=temp:
        cursor.execute("SELECT password FROM data WHERE password in ('{}')".format(passwordE.get()))
        passwordB=cursor.fetchall()
        if passwordB !=temp:
            cursor.execute("SELECT number FROM data WHERE login in ('{}')".format(loginE.get()))
            number=cursor.fetchall()
            cursor.close()
            myBase.close()
            return number
        else:
            l1.config(text="Złe hasło")
    else:
        l1.config(text="Zły login")
    #close connecting
    cursor.close()
    myBase.close()