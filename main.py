from tkinter import *
import time, sys
import pymysql as p
import start


class PinFrame():
    def __init__(self, master):
        #Create frame
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
        #Create frame
        self.number = number
        self.master = master
        self.master.title("BANK")
        self.master.minsize(1000, 600)
        self.master.maxsize(1000, 600)
        self.fMainB = Frame(self.master)
        self.fMainB.pack()

        #Connect with data base
        try:
            myBase = p.connect(host="localhost", user="root", db="bank")
        except:
            self.connectionErrorL = Label(self.fMainB, text="Nie udało się połączyć z bazą danych")
            self.connectionErrorL.grid()
            master.after(4000, master.destroy)
        cursor = myBase.cursor()

        #checking balance
        cursor.execute("SELECT balance FROM data WHERE number={}".format(number))
        accountBalanceB = cursor.fetchall()
        for ch in accountBalanceB:
            for v in ch:
                self.accountBalance=v

        #Menu GUI
        self.l1 = Label(self.fMainB, text="BANK BŁAŻEJA POLSKI")
        self.l1.grid()
        self.accountBalanceL = Label(self.fMainB, text="Stan konta {}".format(self.accountBalance))
        self.transferB = Button(self.fMainB, text="Przelew", command=lambda choice = "Transfer(self.master, self.number)" : self.choiceMenu(choice))
        self.historyB = Button(self.fMainB, text="Historia przelewów", command=lambda choice = "History(self.master, self.number)" : self.choiceMenu(choice))
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
        #Create frame
        self.fMainI = Frame(master)
        self.fMainI.pack()
        #Connect with data base
        try:
            myBase = p.connect(host="localhost", user="root", db="bank")
        except:
            self.connectionErrorL = Label(self.fMainI, text="Nie udało się połączyć z bazą danych")
            self.connectionErrorL.grid()
            master.after(4000, master.destroy)
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

class History (MainFrame):
    def __init__ (self, master, number):
        #Create frame
        self.fMainH = Frame(master)
        self.fMainH.pack()
        #Variables
        theDate=[]
        accountNumber=[]
        amount=[]
        comment=[]
            
        #Connect with data base
        try:
            myBaseH = p.connect(host="localhost", user="root", db="bank")
        except:
            self.connectionErrorL = Label(self.fMainH, text="Nie udało się połączyć z bazą danych")
            self.connectionErrorL.grid()
            master.after(4000, master.destroy)
        cursor = myBaseH.cursor()
            
        try:
            #Import date
            cursor.execute("SELECT date FROM `{}`".format(number))
            dateB = cursor.fetchall()
            for ch in dateB:
                for v in ch:
                    theDate.append(v)
                
            #Import accountNumber
            cursor.execute("SELECT accountNumber FROM `{}`".format(number))
            accountNumberB = cursor.fetchall()
            for ch in accountNumberB:
                for v in ch:
                    accountNumber.append(v)
            #Import amount
            cursor.execute("SELECT amount FROM `{}`".format(number))
            amountB = cursor.fetchall()
            for ch in amountB:
                for v in ch:
                    amount.append(v)
            #Import comment
            cursor.execute("SELECT comment FROM `{}`".format(number))
            commentB = cursor.fetchall()
            for ch in commentB:
                for v in ch:
                    comment.append(v)
            #Import counter
            cursor.execute("SELECT COUNT(*) FROM `{}`".format(number))
            counterB=cursor.fetchall()
            for ch in counterB:
                for v in ch:
                    counter=v
        except:
            self.returnError(master, number)
        
        if counter == 0:
            self.errorL = Label(self.fMainH, text="Historia jest pusta")
            self.returnB2 = Button(self.fMainH, text="Powrót", command=lambda: self.returnError2(master, number))
            self.errorL.grid()
            self.returnB2.grid()
        else:
            #Print history
            for i in range(counter):
                self.counterL = Label(self.fMainH, text="Przelew nr {}".format(i+1))
                self.theDateL = Label(self.fMainH, text="Data: {}".format(theDate[i]))
                self.accountNumberLH = Label(self.fMainH, text="Adres: {}".format(accountNumber[i]))
                self.amountL = Label(self.fMainH, text="Kwota: {} zł".format(amount[i]))
                self.commentL = Label(self.fMainH, text="Komentarz: {}".format(comment[i]))
                self.counterL.grid()
                self.theDateL.grid()
                self.accountNumberLH.grid()
                self.amountL.grid()
                self.commentL.grid()
            self.returnB = Button(self.fMainH, text="Powrót", command=lambda: self.returnF(master, number))
            self.returnB.grid()

    def returnF(self, master, number):

        self.fMainH.destroy()
        self.counterL.destroy()
        self.theDateL.destroy()
        self.accountNumberLH.destroy()
        self.amountL.destroy()
        self.commentL.destroy()
        self.returnB.destroy()
        MainFrame.__init__(self, master, number)
    
    def returnError(self, master, number):
        self.fMainH.destroy()
        MainFrame.__init__(self, master, number)
    
    def returnError2(self, master, number):
        self.fMainH.destroy()
        self.returnB2.destroy()
        self.errorL.destroy()
        MainFrame.__init__(self, master, number)
 
class Transfer (MainFrame):
    def __init__(self, master, number):
        try: 
            self.errorLabel.destroy()
        except:
            #Create frame
            self.fMainT = Frame(master)
            self.fMainT.pack()
            self.date = date=time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
            #Connect with data base
            try:
                self.myBaseT = p.connect(host="localhost", user="root", db="bank")
            except:
                self.connectionErrorL = Label(self.fMainB, text="Nie udało się połączyć z bazą danych")
                self.connectionErrorL.grid()
                master.after(4000, master.destroy)
            self.cursor = self.myBaseT.cursor()

            #checking balance
            self.cursor.execute("SELECT balance FROM data WHERE number={}".format(number))
            accountBalanceB = self.cursor.fetchall()
            for ch in accountBalanceB:
                for v in ch:
                    self.accountBalance=v

            self.accountBalanceLT = Label(self.fMainT, text="Stan konta: {} zł".format(self.accountBalance))
            self.nrOfTL = Label(self.fMainT, text="Numer konta odbiorcy ")
            self.nrOfTE = Entry(self.fMainT)
            self.howMuchL = Label(self.fMainT, text="Kwota przelewu")
            self.howMuchE = Entry(self.fMainT)
            self.comL = Label(self.fMainT, text="Komentarz do przelewu")
            self.comE = Entry(self.fMainT)
            self.confirmB = Button(self.fMainT, text="Wyślij", command = lambda: self.confirmF(master, number))
            self.accountBalanceLT.grid(row=0, columnspan=2)
            self.nrOfTL.grid(row=1, column=0)
            self.nrOfTE.grid(row=1, column=1)
            self.howMuchL.grid(row=2, column=0)
            self.howMuchE.grid(row=2, column=1)
            self.comL.grid(row=3, column=0)
            self.comE.grid(row=3, column=1)
            self.confirmB.grid(row=4, columnspan=2)

    def confirmF(self, master, number):
        if int(self.howMuchE.get()) > self.accountBalance:
            self.errorLabel= Label(self.fMainT, text="Podana kwota jest większa od stanu konta")
            self.errorLabel.grid(row=5, columnspan=2)
            return
        else:
            self.transferL = Label(self.fMainT, text="Wysyłanie przelewu pod numer: {}, o kwocie: {} zł, z komentarzem: {}".format(self.nrOfTE.get(),self.howMuchE.get(), self.comE.get()))
            self.transferL.grid(row=5, columnspan=2)
            #change balance
            self.accountBalance -= int(self.howMuchE.get())
            self.cursor.execute("UPDATE data SET balance = {} WHERE number={}".format(self.accountBalance, number))
            self.myBaseT.commit()
            #saving history
            self.cursor.execute("INSERT INTO `{}`(date, accountNumber, amount, comment) VALUES ('{}' , '{}' , {} , '{}')".format(number, self.date, self.nrOfTE.get(), int(self.howMuchE.get()), self.comE.get()))
            self.myBaseT.commit()
            self.cursor.close()
            self.myBaseT.close()
            master.after(2000, self.returnF(master, number))
    def returnF(self, master, number):
        self.fMainT.destroy()
        self.accountBalanceLT.destroy()
        self.nrOfTL.destroy()
        self.nrOfTE.destroy()
        self.howMuchL.destroy()
        self.howMuchE.destroy()
        self.comL.destroy()
        self.comE.destroy()
        self.confirmB.destroy()
        self.transferL.destroy()
        MainFrame.__init__(self, master, number)
    



root = Tk()
root.minsize(500, 400)
root.maxsize(500, 400)
root.title("BANK - pin")
  
framePin = PinFrame(root)

root.mainloop()