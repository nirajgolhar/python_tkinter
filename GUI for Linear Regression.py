from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import scipy.stats

root = Tk()
root.geometry("800x500")



class First:
    def __init__(self):
        self.x = []
        self.y = []
        self.x_no = IntVar()
        self.x_sq = []
        self.x_y = []
        self.xq = IntVar()
        self.xandy = IntVar()
        self.sumofx = IntVar()
        self.sumofy = IntVar()
        self.sumofxsq = IntVar()
        self.a = DoubleVar()
        self.a1 = IntVar()
        self.a2 = IntVar()
        self.a3 = IntVar()
        self.a4 = IntVar()
        self.a5 = IntVar()
        self.a6 = IntVar()
        self.b = DoubleVar()
        self.b1 = DoubleVar()
        self.b2 = DoubleVar()
        self.y_pred = []
        self.y_pre = DoubleVar()
        ButtonForecasting = Button(root, text='Calculate regression', command=self.regression, fg="blue")
        ButtonForecasting.grid(row=20, column=1)
        ButtonGraph = Button(root, text='Graph', command=self.graph)
        ButtonGraph.grid(row=70, column=1)

        lblEnterXNo = Label(root, text="Enter number of x :", fg="blue")
        lblEnterXNo.grid(row=0, column=0)
        EntryForX = Entry(root, textvariable=self.x_no)
        EntryForX.grid(row=0, column=1)
        self.var1 = self.x_no.get()
        self.y_no = IntVar()
        lblEnterYNo = Label(root, text="Enter number of y :", fg="blue")
        lblEnterYNo.grid(row=1, column=0)
        EntryForY = Entry(root, textvariable=self.y_no)
        EntryForY.grid(row=1, column=1)
        self.var2 = self.y_no.get()
        ButtonDone = Button(root, text='Done', command=self.done)
        ButtonDone.grid(row=5, column=1)
        self.al = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']
        self.bl = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10']



    def regression(self):
        self.calculation()
        # self.newwin = Toplevel(root)
        # self.newwin.geometry("800x250")
        lblclm1 = Label(root, text="X", bd=12, font=("Arial", 10), fg="red")
        lblclm1.grid(row=22, column=0)
        lblclm2 = Label(root, text="Y", bd=12, font=("Arial", 10), fg="red")
        lblclm2.grid(row=22, column=1)
        lblclm3 = Label(root, text="X*X", bd=12, font=("Arial", 10), fg="red")
        lblclm3.grid(row=22, column=2)
        lblclm4 = Label(root, text="X*Y", bd=12, font=("Arial", 10), fg="red")
        lblclm4.grid(row=22, column=3)
        # for x square calculation
        for p in range(0, self.x_no.get()):
            self.xq = (self.x[p] * self.x[p])
            self.x_sq.append(self.xq)
            print(self.x_sq)
        # for x * y calculation
        for q in range(0, self.y_no.get()):
            self.xandy = (self.x[q] * self.y[q])
            self.x_y.append(self.xandy)
            print(self.x_y)
        self.sumofx = sum(self.x)
        print(self.sumofx)
        self.sumofy = sum(self.y)
        print(self.sumofy)
        self.sumofxsq = sum(self.x_sq)
        print(self.sumofxsq)
        self.sumofxandy = sum(self.x_y)
        print(self.sumofxandy)

        # for printing all calculated values in table
        for z in range(0, self.x_no.get()):
            xz = Label(root, text=self.x[z])
            xz.grid(row=23 + z, column=0)
            yz = Label(root, text=self.y[z])
            yz.grid(row=23 + z, column=1)
            wz = Label(root, text=self.x_sq[z])
            wz.grid(row=23 + z, column=2)
            zz = Label(root, text=self.x_y[z])
            zz.grid(row=23 + z, column=3)
            lblsumofx = Label(root, text=self.sumofx)
            lblsumofx.grid(row=23 + (z + 1), column=0)
            lblsumofy = Label(root, text=self.sumofy)
            lblsumofy.grid(row=23 + (z + 1), column=1)
            lblsumofxsq = Label(root, text=self.sumofxsq)
            lblsumofxsq.grid(row=23 + (z + 1), column=2)
            lblsumofxandy = Label(root, text=self.sumofxandy)
            lblsumofxandy.grid(row=23 + (z + 1), column=3)
        lblprinteq = Label(root, text="Equation of straight line:y=ax+b")
        lblprinteq.grid(row=35, column=0)
        self.a1 = self.sumofx * self.sumofx
        print(self.a1)
        self.a2 = self.var1 * self.sumofxsq
        print(self.a2)
        self.a3 = self.sumofx * self.sumofy
        print(self.a3)
        self.a4 = self.var1 * self.sumofxandy
        print(self.a4)
        self.a5 = self.a2 - self.a1
        print(self.a5)
        self.a6 = self.a4 - self.a3
        print(self.a6)
        self.a = self.a6 / self.a5
        print(self.a)
        lblformulafora = Label(root, text="a=x*(sumofxiny)-[(sumofx)*(sumofy)]/[(x*sumofxsq)-(sumofx*sumofx)]")
        lblformulafora.grid(row=45)
        lblvalueforaprint = Label(root, text="value of a")
        lblvalueforaprint.grid(row=50, column=0)
        lblvaluefora = Label(root, text=self.a)
        lblvaluefora.grid(row=50, column=1)
        self.b1 = self.a * self.sumofx
        print(self.b1)
        self.b2 = self.sumofy - self.b1
        print(self.b2)
        self.b = self.b2 / self.var1
        print(self.b)
        lblformulaforb = Label(root, text="b=1/x[sumofy - (a*(sumofx))]")
        lblformulaforb.grid(row=55)
        lblvalueforbprint = Label(root, text="value of b")
        lblvalueforbprint.grid(row=60, column=0)
        lblvalueforb = Label(root, text=self.b)
        lblvalueforb.grid(row=60, column=1)

    def done(self):
        lblEnterX = Label(root, text="Enter X", fg="red")
        lblEnterX.grid(row=9, column=1)
        lblEnterY = Label(root, text="Enter Y", fg="red")
        lblEnterY.grid(row=9, column=2)
        self.var1 = self.x_no.get()
        self.var2 = self.y_no.get()
        print(self.var1)
        print(self.var2)
        if (self.var1 > 10):
            messagebox.showinfo("Error", "Input number less than 11 ", fg="blue", bd=15, font=("Arial", 12))
            root.destroy()
        for i in range(0, self.var1):
            self.al[i] = DoubleVar()
            self.ei = Entry(root, textvariable=self.al[i])
            self.ei.grid(row=i + 12, column=1)

        for k in range(0, self.var1):
            self.bl[k] = DoubleVar()
            self.fk = Entry(root, textvariable=self.bl[k])
            self.fk.grid(row=k + 12, column=2)


    def graph(self):
        plt.scatter(self.x[0:], self.y[0:], color="m", marker="o", s=30)
        plt.plot(self.x, self.y, color="g")
        plt.show()

        for r in range(1, self.var1):
             print(self.b)
             print(self.x[r])
             print(self.a)
             print(type(self.x[r]))
             self.y_pre = self.b + self.a * self.x[r]
             self.y_pred.append(self.y_pre)
             print(self.y_pred)


    def calculation(self):
        for i in range(0, self.var1):
            self.x.append(self.al[i].get())
        for k in range(0, self.var2):
            self.y.append(self.bl[k].get())

        print(self.x[0:])
        print(self.y[0:])




f = First()
root.mainloop()
