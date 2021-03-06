from tkinter import *
import time
import pymysql as p

class MainFrame():
    def __init__(self ,master ,number):
        #Create frame
        self.cos = self
        self.master = master
        self.master.iconbitmap("C:/Users/bkwia/Desktop/python/bankGUI/data/bank.ico")
        self.master.title("BANK")
        self.master.minsize(1000, 600)
        self.master.maxsize(1000, 600)
        self.number = number
        self.fMainB = Frame(self.master, bg="#D2D2D2")
        self.fMainB.place(width=1000, height=600)
        self.fNav = Frame(self.fMainB, bg="#83AD87")
        self.fNav.place(x=0, y=0, width=160, height=600)
        self.fUp = Frame(self.fMainB, bg="#E0E0E0")
        self.fUp.place(x=160, y=0, width=840, height=90)
        self.fContainerBallance = Frame(self.fMainB, bg="#C4C4C4")
        self.fContainerBallance.place(x=230, y=114, width=700, height=200)
        
        #Image
        self.imageExit = PhotoImage(file = "C:/Users/bkwia/Desktop/python/bankGUI/data/exitImage.png")
        self.imageSettings = PhotoImage(file = "C:/Users/bkwia/Desktop/python/bankGUI/data/settingsImage.png")
        self.imageTransfer = PhotoImage(file = "C:/Users/bkwia/Desktop/python/bankGUI/data/transferImage.png")
        self.imageContact = PhotoImage(file="C:/Users/bkwia/Desktop/python/bankGUI/data/contactsImage.png")
        self.imageHistory = PhotoImage(file="C:/Users/bkwia/Desktop/python/bankGUI/data/historyImage.png")
        self.imageInfo = PhotoImage(file="C:/Users/bkwia/Desktop/python/bankGUI/data/myAccountImage.png")
        #Connect with data base
        try:
            myBase = p.connect(host="localhost", user="root", db="bank")
        except:
            self.connectionErrorL = Label(self.fMainB, text="NIE UDAŁO SIĘ POLĄCZYĆ Z BAZĄ DANYCH", font=("K2D", 24, "bold"), bg="#C4C4C4")
            self.connectionErrorL.place(x=230, y=114, width=700, height=200)
            self.master.after(4000, self.master.destroy)
        cursor = myBase.cursor()

        #checking balance
        cursor.execute("SELECT balance FROM data WHERE number={}".format(self.number))
        accountBalanceB = cursor.fetchall()
        for ch in accountBalanceB:
            for v in ch:
                self.accountBalance=v

        #Menu GUI
        self.transferF = Frame(self.fMainB, bg="#C4C4C4")
        self.contactF = Frame(self.fMainB, bg="#C4C4C4")
        self.historyF = Frame(self.fMainB, bg="#C4C4C4")
        self.infoF = Frame(self.fMainB, bg="#C4C4C4")
        self.button5 = Frame(self.fMainB, bg="#C4C4C4")
        self.button6 = Frame(self.fMainB, bg="#C4C4C4")
        self.button7 = Frame(self.fMainB, bg="#C4C4C4")
        self.button8 = Frame(self.fMainB, bg="#C4C4C4")
        self.transferL = Label(self.fMainB, image=self.imageTransfer, bg="#C4C4C4")
        self.transferL.bind("<Button-1>", lambda event ,choice = "Transfer(self.master, self.number)" : self.choiceMenu(choice))
        self.contactL = Label(self.fMainB, image=self.imageContact, bg="#C4C4C4")
        self.contactL.bind("<Button-1>", lambda event ,choice = "Contact(self.master, self.number)" : self.choiceMenu(choice))
        self.historyL = Label(self.fMainB, image=self.imageHistory, bg="#C4C4C4")
        self.historyL.bind("<Button-1>", lambda event ,choice = "History(self.master, self.number)" : self.choiceMenu(choice))
        self.infoL = Label(self.fMainB, image=self.imageInfo, bg="#C4C4C4")
        self.infoL.bind("<Button-1>", lambda event ,choice = "Info(self.master, self.number)" : self.choiceMenu(choice))
        self.transferF.place(x=172, y=322, width=198, height=128)
        self.contactF.place(x=378, y=322, width=198, height=128)
        self.historyF.place(x=584, y=322, width=198, height=128)
        self.infoF.place(x=790, y=322, width=198, height=128)
        self.button5.place(x=172, y=464, width=198, height=128)
        self.button6.place(x=378, y=464, width=198, height=128)
        self.button7.place(x=584, y=464, width=198, height=128)
        self.button8.place(x=790, y=464, width=198, height=128)
        self.transferL.place(x=203, y=322, height=128)
        self.contactL.place(x=419, y=332)
        self.historyL.place(x=629, y=329)
        self.infoL.place(x=840, y=328)
        
        self.logo = Label(self.fMainB, text="NARODOWY BANK", font=("K2D", 48, "bold"), bg="#E0E0E0" )
        self.accountBalanceL = Label(self.fMainB, text="DOSTĘPNE ŚRODKI: {} zł".format(self.accountBalance), font=("K2D", 30, "bold"), bg="#C4C4C4")
        self.settingsB = Label(self.fMainB, image=self.imageSettings, bg="#83AD87")
        self.exitB = Label(self.fMainB, image=self.imageExit, bg="#83AD87")
        self.settingsB.bind("<Button-1>", self.settings)
        self.exitB.bind("<Button-1>", self.exitF)
        self.logo.place(x=160, y=0, width=840, height=90)
        self.accountBalanceL.place(x=230, y=114, width=700, height=200)
        self.settingsB.place(x=48, y=14, width=64, height=63)
        self.exitB.place(x=48, y=528, width=64, height=50)
        self.fMainB.mainloop()

    def choiceMenu(self, choice):
        #Destroy Menu GUI
        self.fMainB.destroy()
        self.logo.destroy()
        self.accountBalanceL.destroy()
        self.exitB.destroy()
        self.settingsB.destroy()
        self.transferL.destroy()
        self.contactL.destroy()
        self.historyL.destroy()
        self.infoL.destroy()
        objectM = eval(choice)
    
    def settings(self, event):
        #Create frame
        self.fSettings = Toplevel(self.master, bg="#D2D2D2")
        self.fSettings.minsize(280, 400)
        self.fSettings.maxsize(280, 400)
        self.fSettings.title("BANK - USTAWIENIA")
        self.footer = Frame(self.fSettings, bg="#83AD87")
        self.footer.place(x=0, y=340, width=280, height=60)
        self.soon = Label(self.fSettings, text="SOON")
        self.soon.place(x=46, y=60)
        #Options
        self.returnB = Button(self.fSettings, text="POWRÓT", bg="#FFF8F8", font=("K2D", 12, "bold") ,command=lambda: self.fSettings.destroy())
        self.returnB.place(x=90, y=350, width=100, height=40)
    
    def exitF(self, event):
        self.logo.destroy()
        self.accountBalanceL.destroy()
        self.exitB.destroy()
        self.settingsB.destroy()
        self.transferL.destroy()
        self.contactL.destroy()
        self.historyL.destroy()
        self.infoL.destroy()
        self.goodbayL = Label(self.fMainB, text="ŻEGNAMY", font=("K2D", 30, "bold"), bg="#C4C4C4")
        self.goodbayL.place(x=230, y=114, width=700, height=200)
        self.master.after(2000, self.master.destroy)

class Contact(MainFrame):
    def __init__(self, master, number):
        self.master = master
        self.number = number
        #Create frame 
        self.fMainC = Frame(self.master, bg="#D2D2D2")
        self.fMainC.place(width=1000, height=600)
        self.fNav = Frame(self.fMainC, bg="#83AD87")
        self.fNav.place(x=0, y=0, width=160, height=600)
        self.fUp = Frame(self.fMainC, bg="#E0E0E0")
        self.fUp.place(x=160, y=0, width=840, height=90)
        self.logo = Label(self.fMainC, text="NARODOWY BANK", font=("K2D", 48, "bold"), bg="#E0E0E0" )
        self.logo.place(x=160, y=0, width=840, height=90)

        #Variables
        self.contact = []
        self.imageReturn = PhotoImage(file = "C:/Users/bkwia/Desktop/python/bankGUI/data/backImage.png")
        #Connect with data base
        try:
            myBase = p.connect(host="localhost", user="root", db="bank")
        except:
            self.connectionErrorL = Label(self.fMainC, text="NIE UDAŁO SIĘ POLĄCZYĆ Z BAZĄ DANYCH", font=("K2D", 24, "bold"), bg="#C4C4C4" )
            self.connectionErrorL.place(x=305, y=291, width=550, height=100)
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
        self.scrollbarContact.place(x=840, y=116, width=30, height=450)
        self.contactList = Listbox(self.fMainC, bg="#C4C4C4", highlightcolor="#C4C4C4", font=("K2D", 30, "bold")  , yscrollcommand = self.scrollbarContact.set )
        
        if self.contactTrue == ['']:
            self.contactList.destroy()
            self.scrollbarContact.destroy()
            self.emptyContact = Label(self.fMainC, text="Brak kontaktów", font=("K2D", 40, "bold"), bg="#C4C4C4" )
            self.emptyContact.place(x=305, y=291, width=550, height=100)
        else:
            #Print contact
            for i in range(len(self.contactTrue)):
                self.contactList.insert(END, "{}".format(self.contactTrue[i]))
            self.contactList.place(x=320, y=116, width=520, height=450)
            self.scrollbarContact.config( command = self.contactList.yview )

        self.returnB = Label(self.fMainC, image=self.imageReturn, bg="#83AD87")
        self.returnB.bind("<Button-1>", self.returnF)
        self.returnB.place(x=37, y=515, width=85, height=85)
            

    def returnF(self, event):
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
        self.imageReturn = PhotoImage(file = "C:/Users/bkwia/Desktop/python/bankGUI/data/backImage.png")
        #Create frame
        self.fMainI = Frame(self.master, bg="#D2D2D2")
        self.fMainI.place(width=1000, height=600)
        self.fNav = Frame(self.fMainI, bg="#83AD87")
        self.fNav.place(x=0, y=0, width=160, height=600)
        self.fUp = Frame(self.fMainI, bg="#E0E0E0")
        self.fUp.place(x=160, y=0, width=840, height=90)
        self.logo = Label(self.fMainI, text="NARODOWY BANK", font=("K2D", 48, "bold"), bg="#E0E0E0" )
        self.logo.place(x=160, y=0, width=840, height=90)
        self.container = Frame(self.fMainI, bg="#C4C4C4")
        self.container.place(x=320, y=116, width=520, height=450)
        #Connect with data base
        try:
            myBase = p.connect(host="localhost", user="root", db="bank")
        except:
            self.connectionErrorL = Label(self.fMainI, text="Nie udało się połączyć z bazą danych", font=("K2D", 24, "bold"), bg="#C4C4C4" )
            self.connectionErrorL.place(x=305, y=291, width=550, height=100)
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
        self.loginL = Label(self.fMainI, text="LOGIN - {}".format(self.login), font=("K2D", 16, "bold"), bg="#C4C4C4")
        self.passwordL = Label(self.fMainI, text="HASŁO - POKAŻ HASŁO", font=("K2D", 16, "bold"), bg="#C4C4C4")
        self.passwordL.bind("<Button-1>", self.showPassword)
        self.pinL = Label(self.fMainI, text="PIN - POKAŻ PIN", font=("K2D", 16, "bold"), bg="#C4C4C4")
        self.pinL.bind("<Button-1>", self.showPIN)
        self.balanceL = Label(self.fMainI, text="STAN KONTA - {}".format(self.balance), font=("K2D", 16, "bold"), bg="#C4C4C4")
        self.nameL = Label(self.fMainI, text="IMIĘ - {}".format(self.name), font=("K2D", 16, "bold"), bg="#C4C4C4")
        self.surnameL = Label(self.fMainI, text="NAZWISKO - {}".format(self.surname), font=("K2D", 16, "bold"), bg="#C4C4C4")
        self.dateOfBirthL = Label(self.fMainI, text="DATA URODZENIA - {}".format(self.dateOfBirth), font=("K2D", 16, "bold"), bg="#C4C4C4")
        self.accountNumberL = Label(self.fMainI, text="NUMER KONTA - {}".format(self.accountNumber), font=("K2D", 14, "bold"), bg="#C4C4C4")
        self.loginL.place(x=320, y=141, width=520, height=50)
        self.passwordL.place(x=320, y=191, width=520, height=50)
        self.pinL.place(x=320, y=241, width=520, height=50)
        self.balanceL.place(x=320, y=291, width=520, height=50)
        self.nameL.place(x=320, y=341, width=520, height=50)
        self.surnameL.place(x=320, y=391, width=520, height=50)
        self.dateOfBirthL.place(x=320, y=441, width=520, height=50)
        self.accountNumberL.place(x=320, y=491, width=520, height=50)
        self.returnB = Label(self.fMainI, image=self.imageReturn, bg="#83AD87")
        self.returnB.bind("<Button-1>", self.returnF)
        self.returnB.place(x=37, y=515, width=85, height=85)

    
    def returnF(self, event):
        self.fMainI.destroy()
        self.loginL.destroy()
        self.passwordL.destroy()
        self.pinL.destroy()
        self.balanceL.destroy()
        self.nameL.destroy()
        self.surnameL.destroy()
        self.dateOfBirthL.destroy()
        self.accountNumberL.destroy()
        self.returnB.destroy()
        MainFrame.__init__(self, self.master, self.number)    

    def showPassword(self, event):
        self.passwordL.config(text="HASŁO - {} ".format(self.password))
    def showPIN(self, event):
        self.pinL.config(text="PIN - {} ".format(self.pin))

class History (MainFrame):
    def __init__ (self, master, number):
        self.master = master
        self.number = number
        #Create frame
        self.fMainH = Frame(self.master, bg="#D2D2D2")
        self.fMainH.place(width=1000, height=600)
        self.fNav = Frame(self.fMainH, bg="#83AD87")
        self.fNav.place(x=0, y=0, width=160, height=600)
        self.fUp = Frame(self.fMainH, bg="#E0E0E0")
        self.fUp.place(x=160, y=0, width=840, height=90)
        self.logo = Label(self.fMainH, text="NARODOWY BANK", font=("K2D", 48, "bold"), bg="#E0E0E0" )
        self.logo.place(x=160, y=0, width=840, height=90)
        #Variables
        theDateOutgoing = []
        accountNumberOutgoing = []
        amountOutgoing = []
        commentOutgoing = []
        theDateIncoming = []
        accountNumberIncoming = []
        amountIncoming = []
        commentIncoming = []
        self.imageReturn = PhotoImage(file = "C:/Users/bkwia/Desktop/python/bankGUI/data/backImage.png")
            
        #Connect with data base
        try:
            myBaseH = p.connect(host="localhost", user="root", db="bank")
        except:
            self.connectionErrorL = Label(self.fMainH, text="NIE UDAŁO SIĘ POLĄCZYĆ Z BAZĄ DANYCH", font=("K2D", 12, "bold"),bg="D2D2D2")
            self.connectionErrorL.place(x=392, y=560, width=375, height=40)
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
        self.outgoingL = Label(self.fMainH, text="WYCHODZĄCE", font=("K2D", 13, "bold"), bg="#D2D2D2" )
        self.incomingL = Label(self.fMainH, text="PRZYCHODZĄCE", font=("K2D", 13, "bold"), bg="#D2D2D2" )
        self.scrollbarOutgoing = Scrollbar(self.fMainH)
        self.scrollbarOutgoing.place(x=501, y=154, width=30, height=400)
        self.historyListOutgoing = Listbox(self.fMainH, yscrollcommand = self.scrollbarOutgoing.set, font=("K2D", 11, "bold"), bg="#C4C4C4", highlightcolor="#C4C4C4")
        self.scrollbarIncoming = Scrollbar(self.fMainH)
        self.scrollbarIncoming.place(x=929, y=154, width=30, height=400)
        self.historyListIncoming = Listbox(self.fMainH, yscrollcommand = self.scrollbarIncoming .set, font=("K2D", 11, "bold"), bg="#C4C4C4", highlightcolor="#C4C4C4")
        self.outgoingL.place(x=201, y=102, width=300, height=52)
        self.outgoingL.place(x=629, y=102, width=300, height=52)
        #Print history Outgoing
        for i in range(counterOutgoing):
            self.historyListOutgoing.insert(END, "Przelew nr {}".format(i+1))
            self.historyListOutgoing.insert(END, "Data: {}".format(theDateOutgoing[i]))
            self.historyListOutgoing.insert(END, "Adres: {}".format(accountNumberOutgoing[i]))
            self.historyListOutgoing.insert(END, "Kwota: {} zł".format(amountOutgoing[i]))
            self.historyListOutgoing.insert(END, "Komentarz: {}".format(commentOutgoing[i]))
            self.historyListOutgoing.insert(END, "---------------------------------------------------------")
        self.historyListOutgoing.place(x=201, y=154, width=300, height=400)
        self.scrollbarOutgoing.config( command = self.historyListOutgoing.yview )
        #Print history Incoming
        for i in range(counterIncoming):
            self.historyListIncoming.insert(END, "Przelew nr {}".format(i+1))
            self.historyListIncoming.insert(END, "Data: {}".format(theDateIncoming[i]))
            self.historyListIncoming.insert(END, "Adres: {}".format(accountNumberIncoming[i]))
            self.historyListIncoming.insert(END, "Kwota: {} zł".format(amountIncoming[i]))
            self.historyListIncoming.insert(END, "Komentarz: {}".format(commentIncoming[i]))
        self.historyListIncoming.place(x=629, y=154, width=300, height=400)
        self.scrollbarIncoming.config( command = self.historyListIncoming.yview )

        self.returnB = Label(self.fMainH, image=self.imageReturn, bg="#83AD87")
        self.returnB.bind("<Button-1>", self.returnF)
        self.returnB.place(x=37, y=515, width=85, height=85)

    def returnF(self, event):

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
        self.imageReturn = PhotoImage(file = "C:/Users/bkwia/Desktop/python/bankGUI/data/backImage.png")
        try: 
            self.errorLabel.destroy()
        except:
            #Create frame
            self.fMainT = Frame(master, bg="#D2D2D2")
            self.fMainT.place(width=1000, height=600)
            self.fNav = Frame(self.fMainT, bg="#83AD87")
            self.fNav.place(x=0, y=0, width=160, height=600)
            self.fUp = Frame(self.fMainT, bg="#E0E0E0")
            self.fUp.place(x=160, y=0, width=840, height=90)
            self.logo = Label(self.fMainT, text="NARODOWY BANK", font=("K2D", 48, "bold"), bg="#E0E0E0" )
            self.logo.place(x=160, y=0, width=840, height=90)
            self.container = Frame(self.fMainT, bg="#C4C4C4")
            self.container.place(x=320, y=116, width=520, height=450)
            self.date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
            #Connect with data base
            try:
                self.myBaseT = p.connect(host="localhost", user="root", db="bank")
            except:
                self.connectionErrorL = Label(self.fMainT, text="NIE UDAŁO SIĘ POLĄCZYĆ Z BAZĄ DANYCH", font=("K2D", 24, "bold"), bg="#C4C4C4" )
                self.connectionErrorL.place(x=305, y=291, width=550, height=100)
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

            self.accountBalanceLT = Label(self.fMainT, text="STAN KONTA: {} zł".format(self.accountBalance), font=("K2D", 25, "bold"), bg="#C4C4C4")
            self.contactL = Label(self.fMainT, text="Kontakt", font=("K2D", 16, "bold"), bg="#C4C4C4")
            self.contactE = Entry(self.fMainT, font=("K2D", 13, "bold"), bg="#FFF8F8")
            self.nrOfTL = Label(self.fMainT, text="Numer konta odbiorcy ", font=("K2D", 16, "bold"), bg="#C4C4C4")
            self.nrOfTE = Entry(self.fMainT, font=("K2D", 13, "bold"), bg="#FFF8F8")
            self.nrOfTE.bind("<Button-1>", self.checkContact)
            self.howMuchL = Label(self.fMainT, text="Kwota przelewu", font=("K2D", 16, "bold"), bg="#C4C4C4")
            self.howMuchE = Entry(self.fMainT, font=("K2D", 13, "bold"), bg="#FFF8F8")
            self.comL = Label(self.fMainT, text="Komentarz do przelewu", font=("K2D", 16, "bold"), bg="#C4C4C4")
            self.comE = Entry(self.fMainT, font=("K2D", 13, "bold"), bg="#FFF8F8")
            self.confirmB = Button(self.fMainT, text="Wyślij", command = lambda: self.confirmF(), font=("K2D", 16, "bold"), bg="#FFF8F8")
            self.accountBalanceLT.place(x=320, y=116, width=520, height=50)
            self.contactL.place(x=320, y=192, width=260, height=60)
            self.contactE.place(x=580, y=202, width=241, height=50)
            self.nrOfTL.place(x=320, y=252, width=260, height=60)
            self.nrOfTE.place(x=580, y=262, width=241, height=50)
            self.howMuchL.place(x=320, y=312, width=260, height=60)
            self.howMuchE.place(x=580, y=322, width=241, height=50)
            self.comL.place(x=320, y=372, width=260, height=60)
            self.comE.place(x=580, y=382, width=241, height=50)
            self.confirmB.place(x=480, y=474, width=200, height=50)
            self.returnB = Label(self.fMainT, image=self.imageReturn, bg="#83AD87")
            self.returnB.bind("<Button-1>", self.returnF)
            self.returnB.place(x=37, y=515, width=85, height=85)


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
            self.errorLabel= Label(self.fMainT, text="Podana kwota jest większa od stanu konta", font=("K2D", 10, "bold"), bg="#C4C4C4")
            self.errorLabel.place(x=357, y=432, width=446, height=42)
            return
        else:
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
            self.master.after(2000, self.returnF2())

    def returnF(self, event):
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
        self.returnB.destroy()
        MainFrame.__init__(self, self.master, self.number)
    def returnF2(self):
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
        self.returnB.destroy()
        MainFrame.__init__(self, self.master, self.number)



