import time, os, sys
import pymysql as p
from tkinter import Label

def authentication(master, loginE, passwordE, l1):
    #Create empty tuple
    temp = ()
    #Connect with data base
    try:
        myBase=p.connect(host="localhost", user="root", db="bank")
    except:
        l1.config(text="NIE UDAŁO SIĘ POLĄCZYĆ Z BAZĄ DANYCH")
        master.after(4000, master.destroy)
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
            cursor.execute("SELECT typeOfAccount FROM data WHERE login = '{}'".format(loginE.get()))
            typeOfAccount = cursor.fetchall()
            cursor.close()
            myBase.close()
            return [number, typeOfAccount]
        else:
            l1.config(text="ZŁE HASŁO")
    else:
        l1.config(text="ZŁY LOGIN")
    #close connecting
    cursor.close()
    myBase.close()