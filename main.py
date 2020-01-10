from tkinter import *
import time, sys
import pymysql as p
import start


class PinFrame():
    def __init__(self, master):
        self.master = master
        self.master.minsize(500, 400)
        self.master.maxsize(500, 400)
        self.fMain = Frame(self.master, width=500, height=400)
        self.fMain.pack()
        #Login GUI
        self.loginL = Label(self.fMain, text="Login" )
        self.passwordL = Label(self.fMain, text="Hasło" )
        self.loginE = Entry(self.fMain)
        self.passwordE = Entry(self.fMain, show="*")
        self.l1 = Label(self.fMain, text="Wprowadz poprawny login i hasło")
        self.confirmB = Button(self.fMain, text="Zaloguj", command=lambda:self.checkLogin())
        self.loginL.grid(column=0, row=0)
        self.passwordL.grid(column=0, row=1)
        self.loginE.grid(column=1, row=0)
        self.passwordE.grid(column=1, row=1)
        self.l1.grid(row=3, columnspan=2)
        self.confirmB.grid( row=4, columnspan=2)


    def checkLogin(self):
        self.number = start.authentication(self.master,self.loginE, self.passwordE, self.l1)
        for ch in self.number:
            for v in ch:
                self.number=v
        self.fMain.destroy()
        self.loginL.destroy()
        self.loginE.destroy()
        self.passwordL.destroy()
        self.passwordE.destroy()
        self.l1.destroy()
        self.confirmB.destroy()
        mainMenu=MainFrame(self.master, self.number)

class MainFrame(PinFrame):
    def __init__(self, master, number):

        #Connect with data base
        try:
            myBase = p.connect(host="localhost", user="root", db="bank")
        except:
            print("Nie udało połączyć się z bazą danych")
            time.sleep(2)
            sys.exit()
        cursor = myBase.cursor()

        #checking balance
        cursor.execute("SELECT balance FROM data WHERE number={}".format(number))
        accountBalanceB = cursor.fetchall()
        for ch in accountBalanceB:
            for v in ch:
                self.accountBalance=v
        self.number = number
        self.master = master
        self.master.title("BANK")
        self.master.minsize(1000, 600)
        self.master.maxsize(1000, 600)
        self.fMainB = Frame(self.master)
        self.fMainB.pack()
        #Menu GUI
        self.l1 = Label(self.fMainB, text="BANK BŁAŻEJA POLSKI")
        self.l1.grid()
        self.accountBalanceL = Label(self.fMainB, text="Stan konta {}".format(self.accountBalance))
        self.transferB = Button(self.fMainB, text="Przelew")
        self.historyB = Button(self.fMainB, text="Historia przelewów")
        self.infoB = Button(self.fMainB, text="Informacje o koncie", command=lambda choice = "Info(self.master, self.number)" : self.choiceMenu(choice))
        self.logoutB = Button(self.fMainB, text="Wyloguj", command= lambda: self.logout() )
        self.exitB = Button(self.fMainB, text="Wyjście", command= lambda: self.exitF())
        self.accountBalanceL.grid()
        self.transferB.grid()
        self.historyB.grid()
        self.infoB.grid() 
        self.logoutB.grid()
        self.exitB.grid()
        self.fMainB.mainloop()

    def choiceMenu(self, choice):
        #Destroy Menu GUI
        self.fMainB.destroy()
        self.l1.destroy()
        self.accountBalanceL.destroy()
        self.transferB.destroy()
        self.historyB.destroy()
        self.infoB.destroy()
        self.logoutB.destroy()
        self.exitB.destroy()
        objectM = eval(choice)
    
    def logout(self):
        #Destroy Menu GUI
        self.fMainB.destroy()
        self.l1.destroy()
        self.accountBalanceL.destroy()
        self.transferB.destroy()
        self.historyB.destroy()
        self.infoB.destroy()
        self.logoutB.destroy()
        self.exitB.destroy()
        PinFrame.__init__(self, self.master) 
    
    def exitF(self):
        self.l1.destroy()
        self.accountBalanceL.destroy()
        self.transferB.destroy()
        self.historyB.destroy()
        self.infoB.destroy()
        self.logoutB.destroy()
        self.exitB.destroy()
        self.goodbayL = Label(self.fMainB, text="Żegnamy")
        self.goodbayL.grid()
        self.master.after(2000, self.master.destroy)


class Info(MainFrame):
    def __init__(self, master,number):
        
        #Connect with data base
        try:
            myBase = p.connect(host="localhost", user="root", db="bank")
        except:
            print("Nie udało połączyć się z bazą danych")
            time.sleep(2)
            sys.exit()
        cursor = myBase.cursor()

        #import login
        cursor.execute("SELECT login FROM data WHERE number = {}".format(number))
        loginT=cursor.fetchall()
        for ch in loginT:
            for v in ch:
                login=v
        #import password
        cursor.execute("SELECT password FROM data WHERE number = {}".format(number))
        passwordT=cursor.fetchall()
        for ch in passwordT:
            for v in ch:
                password=v
        #import pin
        cursor.execute("SELECT pin FROM data WHERE number = {}".format(number))
        pinT=cursor.fetchall()
        for ch in pinT:
            for v in ch:
                pin=v
        #import balance
        cursor.execute("SELECT balance FROM data WHERE number = {}".format(number))
        balanceT=cursor.fetchall()
        for ch in balanceT:
            for v in ch:
                balance=v
        #import name
        cursor.execute("SELECT name FROM data WHERE number = {}".format(number))
        nameT=cursor.fetchall()
        for ch in nameT:
            for v in ch:
                name=v
        #import surname
        cursor.execute("SELECT surname FROM data WHERE number = {}".format(number))
        surnameT=cursor.fetchall()
        for ch in surnameT:
            for v in ch:
                surname=v
        #import dateOfBirth
        cursor.execute("SELECT dateOfBirth FROM data WHERE number = {}".format(number))
        dateOfBirthT=cursor.fetchall()
        for ch in dateOfBirthT:
            for v in ch:
                dateOfBirth=v
        #import accountNumber
        cursor.execute("SELECT accountNumber FROM data WHERE number = {}".format(number))
        accountNumberT=cursor.fetchall()
        for ch in accountNumberT:
            for v in ch:
                accountNumber=v

        #Info GUI
        self.fMainI = Frame(master)
        self.fMainI.pack()
        self.loginL = Label(self.fMainI, text="Login - {}".format(login))
        self.passwordL = Label(self.fMainI, text="Hasło - {}".format(password))
        self.pinL = Label(self.fMainI, text="PIN - {}".format(pin))
        self.balanceL = Label(self.fMainI, text="Stan konta - {}".format(balance))
        self.nameL = Label(self.fMainI, text="Imie - {}".format(name))
        self.surnameL = Label(self.fMainI, text="Naziwsko - {}".format(surname))
        self.dateOfBirthL = Label(self.fMainI, text="Data urodzenia - {}".format(dateOfBirth))
        self.accountNumberL = Label(self.fMainI, text="Numer konta - {}".format(accountNumber))
        self.backB = Button(self.fMainI, text="Powrót", command= lambda:self.returnF(master, number))
        self.loginL.grid()
        self.passwordL.grid()
        self.pinL.grid()
        self.balanceL.grid()
        self.nameL.grid()
        self.surnameL.grid()
        self.dateOfBirthL.grid()
        self.accountNumberL.grid()
        self.backB.grid()

    
    def returnF(self, master, number):
        self.fMainI.destroy()
        self.loginL.destroy()
        self.passwordL.destroy()
        self.pinL.destroy()
        self.balanceL.destroy()
        self.nameL.destroy()
        self.surnameL.destroy()
        self.dateOfBirthL.destroy()
        self.accountNumberL.destroy()
        self.backB.destroy()
        MainFrame.__init__(self, master, number)    

 
       
 
 
root = Tk()
root.minsize(500, 400)
root.maxsize(500, 400)
root.title("BANK - pin")
  
framePin = PinFrame(root)

root.mainloop()