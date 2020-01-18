from tkinter import *
import time
import pymysql as p

class AdminMainFrame():
    def __init__(self ,master ,number):
        #Create frame
        self.cos = self
        self.master = master
        self.master.iconbitmap("C:/Users/bkwia/Desktop/python/bankGUI/data/bank.ico")
        self.master.title("BANK - Admin")
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
        
        self.logo = Label(self.fMainB, text="NARODOWY BANK", font=("K2D", 48, "bold"), bg="#E0E0E0" )
        self.accountBalanceL = Label(self.fMainB, text="DOSTĘPNE ŚRODKI: {} zł".format(self.accountBalance), font=("K2D", 30, "bold"), bg="#C4C4C4")
        self.transferB = Button(self.fMainB, text="PRZELEW",bg="#FFF8F8", font=("K2D", 12, "bold"), command=lambda choice = "Transfer(self.master, self.number)" : self.choiceMenu(choice))
        self.contactB = Button(self.fMainB, text="KONTAKTY",bg="#FFF8F8", font=("K2D", 12, "bold"), command=lambda choice = "Contact(self.master, self.number)" : self.choiceMenu(choice))
        self.historyB = Button(self.fMainB, text="HISTORIA",bg="#FFF8F8", font=("K2D", 12, "bold"), command=lambda choice = "History(self.master, self.number)" : self.choiceMenu(choice))
        self.infoB = Button(self.fMainB, text="KONTO",bg="#FFF8F8", font=("K2D", 12, "bold"), command=lambda choice = "Info(self.master, self.number)" : self.choiceMenu(choice))
        self.settingsB = Button(self.fMainB, text="USTAWIENIA", bg="#FFF8F8", font=("K2D", 6, "bold"), command= lambda: self.settings())
        self.exitB = Button(self.fMainB, text="WYJDŹ",bg="#FFF8F8", font=("K2D", 8, "bold"), command= lambda: self.exitF())
        self.logo.place(x=160, y=0, width=840, height=90)
        self.accountBalanceL.place(x=230, y=114, width=700, height=200)
        self.transferB.place(x=30, y=22, width=100, height=80)
        self.contactB.place(x=30, y=124, width=100, height=80)
        self.historyB.place(x=30, y=226, width=100, height=80)
        self.infoB.place(x=30, y=328, width=100, height=80) 
        self.settingsB.place(x=50, y=476, width=60, height=40)
        self.exitB.place(x=50, y=530, width=60, height=40)
        self.fMainB.mainloop()

    def choiceMenu(self, choice):
        #Destroy Menu GUI
        self.fMainB.destroy()
        self.logo.destroy()
        self.accountBalanceL.destroy()
        self.transferB.destroy()
        self.historyB.destroy()
        self.infoB.destroy()
        self.exitB.destroy()
        self.settingsB.destroy()
        self.contactB.destroy()
        objectM = eval(choice)
    
    def settings(self):
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
    
    def exitF(self):
        self.logo.destroy()
        self.accountBalanceL.destroy()
        self.transferB.destroy()
        self.historyB.destroy()
        self.infoB.destroy()
        self.exitB.destroy()
        self.contactB.destroy()
        self.settingsB.destroy()
        self.goodbayL = Label(self.fMainB, text="ŻEGNAMY", font=("K2D", 30, "bold"), bg="#C4C4C4")
        self.goodbayL.place(x=230, y=114, width=700, height=200)
        self.master.after(2000, self.master.destroy)