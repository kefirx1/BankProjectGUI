from tkinter import *
import time, sys, start
import pymysql as p



class StartFrame():
    def __init__(self, master):
        #Create frame
        self.master = master
        self.master.title("BANK - pin")
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
        self.exitB = Button(self.fMain, text="Wyjdź", command= lambda: self.master.destroy())
        self.loginL.grid(column=0, row=0)
        self.passwordL.grid(column=0, row=1)
        self.loginE.grid(column=1, row=0)
        self.passwordE.grid(column=1, row=1)
        self.l1.grid(row=3, columnspan=2)
        self.confirmB.grid( row=4, columnspan=2)
        self.exitB.grid(row=5, columnspan=2)


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

class MainFrame(StartFrame):
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
            self.master.after(4000, self.master.destroy)
        cursor = myBase.cursor()

        #checking balance
        cursor.execute("SELECT balance FROM data WHERE number={}".format(self.number))
        accountBalanceB = cursor.fetchall()
        for ch in accountBalanceB:
            for v in ch:
                self.accountBalance=v

        #Menu GUI
        self.l1 = Label(self.fMainB, text="BANK BŁAŻEJA POLSKI")
        self.l1.grid()
        self.accountBalanceL = Label(self.fMainB, text="Stan konta {}".format(self.accountBalance))
        self.transferB = Button(self.fMainB, text="Przelew", command=lambda choice = "Transfer(self.master, self.number)" : self.choiceMenu(choice))
        self.contactB = Button(self.fMainB, text="Kontakty", command=lambda choice = "Contact(self.master, self.number)" : self.choiceMenu(choice))
        self.historyB = Button(self.fMainB, text="Historia przelewów", command=lambda choice = "History(self.master, self.number)" : self.choiceMenu(choice))
        self.infoB = Button(self.fMainB, text="Informacje o koncie", command=lambda choice = "Info(self.master, self.number)" : self.choiceMenu(choice))
        self.logoutB = Button(self.fMainB, text="Wyloguj", command= lambda: self.logout() )
        self.exitB = Button(self.fMainB, text="Wyjście", command= lambda: self.exitF())
        self.accountBalanceL.grid()
        self.transferB.grid()
        self.contactB.grid()
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
        self.contactB.destroy()
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
        self.contactB.destroy()
        StartFrame.__init__(self, self.master) 
    
    def exitF(self):
        self.l1.destroy()
        self.accountBalanceL.destroy()
        self.transferB.destroy()
        self.historyB.destroy()
        self.infoB.destroy()
        self.logoutB.destroy()
        self.exitB.destroy()
        self.contactB.destroy()
        self.goodbayL = Label(self.fMainB, text="Żegnamy")
        self.goodbayL.grid()
        self.master.after(2000, self.master.destroy)

class Contact(MainFrame):
    def __init__(self, master, number):
        self.master = master
        self.number = number
        #Create frame 
        self.fMainC = Frame(self.master)
        self.fMainC.pack()
        #Variables
        self.contact = []
        #Connect with data base
        try:
            myBase = p.connect(host="localhost", user="root", db="bank")
        except:
            self.connectionErrorL = Label(self.fMainC, text="Nie udało się połączyć z bazą danych")
            self.connectionErrorL.grid()
            self.master.after(4000, self.master.destroy)
        self.cursor = myBase.cursor()
        
        try:
            #Import contact
            self.cursor.execute("SELECT contact FROM `{}` ".format(self.number))
            self.contactB = self.cursor.fetchall()
            for ch in self.contactB:
                for v in ch:
                    self.contact.append(v)
        except:
            pass

        #Check multiple contact
        self.contactTemp = []
        self.contactTrue = []
        for i in self.contact:
            if i in self.contactTemp:
                continue
            else:
                self.contactTrue.append(i)
                self.contactTemp.append(i)

        #Create scrollbars
        self.scrollbarContact = Scrollbar(self.fMainC)
        self.scrollbarContact.grid(row=0, column=1, sticky=N+S)
        self.contactList = Listbox(self.fMainC, yscrollcommand = self.scrollbarContact.set )
        
        if self.contactTrue == ['']:
            self.contactList.destroy()
            self.scrollbarContact.destroy()
            self.emptyContact = Label(self.fMainC, text="Brak kontaktów")
            self.emptyContact.grid()
        else:
            #Print contact
            for i in range(len(self.contactTrue)):
                self.contactList.insert(END, "Kontakt nr {}: {}".format(i+1, self.contactTrue[i]))
            self.contactList.grid(row=0, column=0)
            self.scrollbarContact.config( command = self.contactList.yview )

        self.returnB = Button(self.fMainC, text="Powrót", command=lambda: self.returnF())
        self.returnB.grid(row=1)
            

    def returnF(self):
        self.fMainC.destroy()
        try:
            self.scrollbarContact.destroy()
            self.contactList.destroy()
        except:
            pass
        try:
            self.emptyContact.destroy()
        except:
            pass
        self.returnB.destroy()
        MainFrame.__init__(self, self.master, self.number) 
    
    def returnError(self):
        self.fMainC.destroy()
        MainFrame.__init__(self, self.master, self.number)

class Info(MainFrame):
    def __init__(self, master,number):
        self.master = master
        self.number = number
        #Create frame
        self.fMainI = Frame(master)
        self.fMainI.pack()
        #Connect with data base
        try:
            myBase = p.connect(host="localhost", user="root", db="bank")
        except:
            self.connectionErrorL = Label(self.fMainI, text="Nie udało się połączyć z bazą danych")
            self.connectionErrorL.grid()
            self.master.after(4000, self.master.destroy)
        cursor = myBase.cursor()

        #import login
        cursor.execute("SELECT login FROM data WHERE number = {}".format(self.number))
        loginT=cursor.fetchall()
        for ch in loginT:
            for v in ch:
                self.login=v
        #import password
        cursor.execute("SELECT password FROM data WHERE number = {}".format(self.number))
        passwordT=cursor.fetchall()
        for ch in passwordT:
            for v in ch:
                self.password=v
        #import pin
        cursor.execute("SELECT pin FROM data WHERE number = {}".format(self.number))
        pinT=cursor.fetchall()
        for ch in pinT:
            for v in ch:
                self.pin=v
        #import balance
        cursor.execute("SELECT balance FROM data WHERE number = {}".format(self.number))
        balanceT=cursor.fetchall()
        for ch in balanceT:
            for v in ch:
                self.balance=v
        #import name
        cursor.execute("SELECT name FROM data WHERE number = {}".format(self.number))
        nameT=cursor.fetchall()
        for ch in nameT:
            for v in ch:
                self.name=v
        #import surname
        cursor.execute("SELECT surname FROM data WHERE number = {}".format(self.number))
        surnameT=cursor.fetchall()
        for ch in surnameT:
            for v in ch:
                self.surname=v
        #import dateOfBirth
        cursor.execute("SELECT dateOfBirth FROM data WHERE number = {}".format(self.number))
        dateOfBirthT=cursor.fetchall()
        for ch in dateOfBirthT:
            for v in ch:
                self.dateOfBirth=v
        #import accountNumber
        cursor.execute("SELECT accountNumber FROM data WHERE number = {}".format(self.number))
        accountNumberT=cursor.fetchall()
        for ch in accountNumberT:
            for v in ch:
                self.accountNumber=v

        #Info GUI
        self.loginL = Label(self.fMainI, text="Login - {}".format(self.login))
        self.passwordL = Label(self.fMainI, text="Hasło - Pokaż hasło")
        self.passwordL.bind("<Button-1>", self.showPassword)
        self.pinL = Label(self.fMainI, text="PIN - Pokaż PIN")
        self.pinL.bind("<Button-1>", self.showPIN)
        self.balanceL = Label(self.fMainI, text="Stan konta - {}".format(self.balance))
        self.nameL = Label(self.fMainI, text="Imie - {}".format(self.name))
        self.surnameL = Label(self.fMainI, text="Naziwsko - {}".format(self.surname))
        self.dateOfBirthL = Label(self.fMainI, text="Data urodzenia - {}".format(self.dateOfBirth))
        self.accountNumberL = Label(self.fMainI, text="Numer konta - {}".format(self.accountNumber))
        self.backB = Button(self.fMainI, text="Powrót", command= lambda:self.returnF())
        self.loginL.grid()
        self.passwordL.grid()
        self.pinL.grid()
        self.balanceL.grid()
        self.nameL.grid()
        self.surnameL.grid()
        self.dateOfBirthL.grid()
        self.accountNumberL.grid()
        self.backB.grid()

    
    def returnF(self):
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
        MainFrame.__init__(self, self.master, self.number)    

    def showPassword(self, event):
        self.passwordL.config(text="Hasło - {} ".format(self.password))
    def showPIN(self, event):
        self.pinL.config(text="PIN - {} ".format(self.pin))

class History (MainFrame):
    def __init__ (self, master, number):
        self.master = master
        self.number = number
        #Create frame
        self.fMainH = Frame(master)
        self.fMainH.pack()
        #Variables
        theDateOutgoing = []
        accountNumberOutgoing = []
        amountOutgoing = []
        commentOutgoing = []
        theDateIncoming = []
        accountNumberIncoming = []
        amountIncoming = []
        commentIncoming = []
            
        #Connect with data base
        try:
            myBaseH = p.connect(host="localhost", user="root", db="bank")
        except:
            self.connectionErrorL = Label(self.fMainH, text="Nie udało się połączyć z bazą danych")
            self.connectionErrorL.grid()
            self.master.after(4000, self.master.destroy)
        cursor = myBaseH.cursor()

        #Import outgoing   
        try:
            #Import date
            cursor.execute("SELECT date FROM `{}` WHERE type='outgoing' ".format(self.number))
            dateB = cursor.fetchall()
            for ch in dateB:
                for v in ch:
                    theDateOutgoing.append(v)
                
            #Import accountNumber
            cursor.execute("SELECT accountNumber FROM `{}` WHERE type='outgoing' ".format(self.number))
            accountNumberB = cursor.fetchall()
            for ch in accountNumberB:
                for v in ch:
                    accountNumberOutgoing.append(v)
            #Import amount
            cursor.execute("SELECT amount FROM `{}` WHERE type='outgoing' ".format(self.number))
            amountB = cursor.fetchall()
            for ch in amountB:
                for v in ch:
                    amountOutgoing.append(v)
            #Import comment
            cursor.execute("SELECT comment FROM `{}` WHERE type='outgoing' ".format(self.number))
            commentB = cursor.fetchall()
            for ch in commentB:
                for v in ch:
                    commentOutgoing.append(v)
            #Import counter
            cursor.execute("SELECT COUNT(*) FROM `{}` WHERE type='outgoing' ".format(self.number))
            counterB=cursor.fetchall()
            for ch in counterB:
                for v in ch:
                    counterOutgoing=v
        except:
            self.returnError()
        #Import incoming
        try:
            #Import date
            cursor.execute("SELECT date FROM `{}` WHERE type='incoming' ".format(self.number))
            dateB = cursor.fetchall()
            for ch in dateB:
                for v in ch:
                    theDateIncoming.append(v)
                
            #Import accountNumber
            cursor.execute("SELECT accountNumber FROM `{}` WHERE type='incoming' ".format(self.number))
            accountNumberB = cursor.fetchall()
            for ch in accountNumberB:
                for v in ch:
                    accountNumberIncoming.append(v)
            #Import amount
            cursor.execute("SELECT amount FROM `{}` WHERE type='incoming' ".format(self.number))
            amountB = cursor.fetchall()
            for ch in amountB:
                for v in ch:
                    amountIncoming.append(v)
            #Import comment
            cursor.execute("SELECT comment FROM `{}` WHERE type='incoming' ".format(self.number))
            commentB = cursor.fetchall()
            for ch in commentB:
                for v in ch:
                    commentIncoming.append(v)
            #Import counter
            cursor.execute("SELECT COUNT(*) FROM `{}` WHERE type='incoming' ".format(self.number))
            counterB=cursor.fetchall()
            for ch in counterB:
                for v in ch:
                    counterIncoming=v
        except:
            self.returnError()
        
        #Create scrollbars
        self.scrollbarOutgoing = Scrollbar(self.fMainH)
        self.scrollbarOutgoing.grid(row=0, column=1, sticky=N+S)
        self.historyListOutgoing = Listbox(self.fMainH, yscrollcommand = self.scrollbarOutgoing.set )
        self.scrollbarIncoming = Scrollbar(self.fMainH)
        self.scrollbarIncoming.grid(row=0, column=3, sticky=N+S)
        self.historyListIncoming = Listbox(self.fMainH, yscrollcommand = self.scrollbarIncoming .set )

        #Print history Outgoing
        for i in range(counterOutgoing):
            self.historyListOutgoing.insert(END, "Przelew nr {}".format(i+1))
            self.historyListOutgoing.insert(END, "Data: {}".format(theDateOutgoing[i]))
            self.historyListOutgoing.insert(END, "Adres: {}".format(accountNumberOutgoing[i]))
            self.historyListOutgoing.insert(END, "Kwota: {} zł".format(amountOutgoing[i]))
            self.historyListOutgoing.insert(END, "Komentarz: {}".format(commentOutgoing[i]))
        self.historyListOutgoing.grid(row=0, column=0)
        self.scrollbarOutgoing.config( command = self.historyListOutgoing.yview )
        #Print history Incoming
        for i in range(counterIncoming):
            self.historyListIncoming.insert(END, "Przelew nr {}".format(i+1))
            self.historyListIncoming.insert(END, "Data: {}".format(theDateIncoming[i]))
            self.historyListIncoming.insert(END, "Adres: {}".format(accountNumberIncoming[i]))
            self.historyListIncoming.insert(END, "Kwota: {} zł".format(amountIncoming[i]))
            self.historyListIncoming.insert(END, "Komentarz: {}".format(commentIncoming[i]))
        self.historyListIncoming.grid(row=0, column=2)
        self.scrollbarIncoming.config( command = self.historyListIncoming.yview )

        self.returnB = Button(self.fMainH, text="Powrót", command=lambda: self.returnF())
        self.returnB.grid(row=1, columnspan=4)

    def returnF(self):

        self.fMainH.destroy()
        self.scrollbarOutgoing.destroy()
        self.historyListOutgoing.destroy()
        self.scrollbarIncoming.destroy()
        self.historyListIncoming.destroy()
        self.returnB.destroy()
        MainFrame.__init__(self, self.master, self.number)
    
    def returnError(self):
        self.fMainH.destroy()
        MainFrame.__init__(self, self.master, self.number)
    
class Transfer (MainFrame):
    def __init__(self, master, number):
        self.master = master
        self.number = number
        try: 
            self.errorLabel.destroy()
        except:
            #Create frame
            self.fMainT = Frame(master)
            self.fMainT.pack()
            self.date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
            #Connect with data base
            try:
                self.myBaseT = p.connect(host="localhost", user="root", db="bank")
            except:
                self.connectionErrorL = Label(self.fMainT, text="Nie udało się połączyć z bazą danych")
                self.connectionErrorL.grid()
                self.master.after(4000, self.master.destroy)
            self.cursor = self.myBaseT.cursor()

            #Contact
            self.contactT = []
            try:
                #Import contact
                self.cursor.execute("SELECT contact FROM `{}` ".format(self.number))
                self.contactBT = self.cursor.fetchall()
                for ch in self.contactBT:
                    for v in ch:
                        self.contactT.append(v)
            except:
                pass

            #Check multiple contact
            self.contactTempT = []
            self.contactTrueT = []
            for i in self.contactT:
                if i in self.contactTempT:
                    continue
                else:
                    self.contactTrueT.append(i)
                    self.contactTempT.append(i)

            #checking balance
            self.cursor.execute("SELECT balance FROM data WHERE number={}".format(self.number))
            accountBalanceB = self.cursor.fetchall()
            for ch in accountBalanceB:
                for v in ch:
                    self.accountBalance=v

            self.accountBalanceLT = Label(self.fMainT, text="Stan konta: {} zł".format(self.accountBalance))
            self.contactL = Label(self.fMainT, text="Kontakt")
            self.contactE = Entry(self.fMainT)
            self.nrOfTL = Label(self.fMainT, text="Numer konta odbiorcy ")
            self.nrOfTE = Entry(self.fMainT)
            self.nrOfTE.bind("<Button-1>", self.checkContact)
            self.howMuchL = Label(self.fMainT, text="Kwota przelewu")
            self.howMuchE = Entry(self.fMainT)
            self.comL = Label(self.fMainT, text="Komentarz do przelewu")
            self.comE = Entry(self.fMainT)
            self.confirmB = Button(self.fMainT, text="Wyślij", command = lambda: self.confirmF())
            self.returnB = Button(self.fMainT, text="Powrót", command = lambda: self.returnF())
            self.accountBalanceLT.grid(row=0, columnspan=2)
            self.contactL.grid(row=1, column=0)
            self.contactE.grid(row=1, column=1)
            self.nrOfTL.grid(row=2, column=0)
            self.nrOfTE.grid(row=2, column=1)
            self.howMuchL.grid(row=3, column=0)
            self.howMuchE.grid(row=3, column=1)
            self.comL.grid(row=4, column=0)
            self.comE.grid(row=4, column=1)
            self.confirmB.grid(row=5, columnspan=2)
            self.returnB.grid(row=6, columnspan=2)

    def checkContact(self, event):
        if self.contactE.get() in self.contactTrueT:
                #import accountNumber:
                try:
                    self.cursor.execute("SELECT accountNumber FROM `{}` WHERE contact = '{}' ".format(self.number, self.contactE.get()))
                    accountNumberPromptE = self.cursor.fetchall()
                    for ch in accountNumberPromptE:
                        for v in ch:
                            self.accountNumberPrompt = v
                except:
                    pass
                self.nrOfTE.delete(0, END)
                self.nrOfTE.insert(0, self.accountNumberPrompt)
                return "break"

    def confirmF(self):
        if int(self.howMuchE.get()) > self.accountBalance:
            self.errorLabel= Label(self.fMainT, text="Podana kwota jest większa od stanu konta")
            self.errorLabel.grid(row=7, columnspan=2)
            return
        else:
            self.transferL = Label(self.fMainT, text="Wysyłanie przelewu pod numer: {}, o kwocie: {} zł, z komentarzem: {}".format(self.nrOfTE.get(),self.howMuchE.get(), self.comE.get()))
            self.transferL.grid(row=7, columnspan=2)

            self.cursor.execute("SELECT accountNumber FROM data WHERE accountNumber= '{}' ".format(self.nrOfTE.get()))
            self.nrOfTDB = self.cursor.fetchall()
            for ch in self.nrOfTDB:
                for v in ch:
                    self.nrOfTDB=v
            if self.nrOfTE.get() == self.nrOfTDB:
                self.cursor.execute("SELECT balance FROM data WHERE accountNumber = '{}' ".format(self.nrOfTE.get()))
                self.balance = self.cursor.fetchall()
                for ch in self.balance:
                    for v in ch:
                        self.balance=v
                        self.newBalance = self.balance + float(self.howMuchE.get())
                self.cursor.execute("UPDATE data SET balance = {} WHERE accountNumber = '{}' ".format(self.newBalance, self.nrOfTE.get()))    
                self.myBaseT.commit()
                self.cursor.execute("SELECT number FROM data WHERE accountNumber = '{}' ".format(self.nrOfTE.get()))
                self.numberTo = self.cursor.fetchall()
                for ch in self.numberTo:
                    for v in ch:
                        self.numberTo=v
                self.cursor.execute("INSERT INTO `{}`(date, accountNumber, amount, comment, type) VALUES ('{}' , '{}' , {} , '{}', '{}')".format(self.numberTo, self.date, self.nrOfTE.get(), float(self.howMuchE.get()), self.comE.get(), "incoming"))
                self.myBaseT.commit()
            #change balance
            self.accountBalance -= int(self.howMuchE.get())
            self.cursor.execute("UPDATE data SET balance = {} WHERE number={}".format(self.accountBalance, self.number))
            self.myBaseT.commit()
            #saving history
            self.cursor.execute("INSERT INTO `{}`(date, accountNumber, contact, amount, comment, type) VALUES ('{}' , '{}' ,'{}', {} , '{}', '{}')".format(self.number, self.date, self.nrOfTE.get(),self.contactE.get(), float(self.howMuchE.get()), self.comE.get(), "outgoing"))
            self.myBaseT.commit()
            self.cursor.close()
            self.myBaseT.close()
            self.master.after(2000, self.returnF())

    def returnF(self):
        self.fMainT.destroy()
        self.accountBalanceLT.destroy()
        self.nrOfTL.destroy()
        self.nrOfTE.destroy()
        self.contactL.destroy()
        self.contactE.destroy()
        self.howMuchL.destroy()
        self.howMuchE.destroy()
        self.comL.destroy()
        self.comE.destroy()
        self.confirmB.destroy()
        try:
            self.transferL.destroy()
        except:
            pass
        self.returnB.destroy()
        MainFrame.__init__(self, self.master, self.number)

if __name__ == "__main__":
    root = Tk()  
    framePin = StartFrame(root)
    root.mainloop()