from tkinter import *
import data.start
import pymysql as p
from mainUser import MainFrame

class StartFrame():
    def __init__(self, master):
        #Create frame
        self.master = master
        self.master.title("BANK - pin")
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)
        self.fMain = Frame(self.master, bg="#83AD87")
        self.fMain.place(width=500, height=300)
        self.fUp = Frame(self.fMain, bg="#D2D2D2")
        self.fUp.place(x=0, y=0, width=500, height=37)
        #Login GUI
        self.logo = Label(self.fMain, text="Narodowy Bank", font=("K2D", 18, "bold"), bg="#D2D2D2")
        self.loginL = Label(self.fMain, text="Login", font=("K2D", 28, "bold"), bg="#83AD87")
        self.passwordL = Label(self.fMain, text="Hasło", font=("K2D", 28, "bold"), bg="#83AD87")
        self.loginE = Entry(self.fMain, font=("K2D", 10, "bold"))
        self.passwordE = Entry(self.fMain, show="*", font=("K2D", 10, "bold"))
        self.l1 = Label(self.fMain, text="Wprowadz poprawny login i hasło", font=("K2D", 9, "bold"), bg="#83AD87")
        self.confirmB = Button(self.fMain, text="Zaloguj", font=("K2D", 18, "bold"),bg="#FFF8F8", command=lambda:self.checkLogin())
        self.exitB = Button(self.fMain, text="Wyjdź", font=("K2D", 18, "bold"),bg="#FFF8F8", command= lambda: self.master.destroy())
        self.logo.place(x=164, y=0, width=180 ,height=36)
        self.loginL.place(x=100, y=80, width=100, height=40)
        self.passwordL.place(x=100, y=136, width=100, height=40)
        self.loginE.place(x=223, y=80, width=130, height=40)
        self.passwordE.place(x=223, y=136, width=130, height=40)
        self.l1.place(x=123, y=192, width=201, height=23)
        self.confirmB.place(x=287, y=228, width=121, height=40)
        self.exitB.place(x=63, y=228, width=121, height=40)


    def checkLogin(self):
        self.number = data.start.authentication(self.master,self.loginE, self.passwordE, self.l1)
        for ch in self.number:
            for v in ch:
                self.number=v
        self.fMain.destroy()
        self.fUp.destroy()
        self.logo.destroy()
        self.loginL.destroy()
        self.passwordL.destroy()
        self.loginE.destroy()
        self.passwordE.destroy()
        self.l1.destroy()
        self.confirmB.destroy()
        self.exitB.destroy()
        mainMenu=MainFrame(self.master, self.number)

if __name__ == "__main__":
    root = Tk()  
    root.iconbitmap("C:/Users/bkwia/Desktop/python/bankGUI/data/bank.ico")
    framePin = StartFrame(root)
    root.mainloop()