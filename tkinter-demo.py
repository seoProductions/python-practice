# Some assignment involving TKinter. This serves as a reference 
# for Python GUI during my the completion of my assigmnets.
#
# Assignment:
# Here, I import all class, function, and contsant definitions from tkinter library
from tkinter import *
# * is the wild card!


class InvestmentValueCalculator():
    def __init__(self):
        self.window = Tk()
        self.window.title = "Investment Calculator"

        #create widgets
        Label(self.window, text="Investment Amont").grid(row=1, column=1, sticky= W)
        Label(self.window, text="Years").grid(row=2, column=1, sticky= W)
        Label(self.window, text="Annual Interest Rate").grid(row=3, column=1, sticky= W)
        Label(self.window, text="Future Value").grid(row=4, column=1, sticky= W)

        #member variables
        self.InvestmentAmount = StringVar()
        self.Years            = StringVar()
        self.AnnualInterestRate = StringVar()
        self.FutureValue = StringVar()

        #create entries
        Entry(self.window, textvariable= self.InvestmentAmount, justify=RIGHT).grid(row=1, column=2)
        Entry(self.window, textvariable= self.Years, justify=RIGHT)          .grid(row=2, column=2)
        Entry(self.window, textvariable= self.AnnualInterestRate, justify=RIGHT).grid(row=3, column=2)
        Label(self.window, textvariable= self.FutureValue, justify=RIGHT).grid(row=4, column=2)

        #create button
        self.button = Button(self.window, text="Calculate", command=self.onClick).grid(row=5,column=1)

        #start loop
        self.window.mainloop()


    def onClick(self):
        self.FutureValue.set(str( \
                float(self.InvestmentAmount) * (1 + float(self.AnnualInterestRate)/12 )**(float(self.Years) * 12.0)
        ))


program = InvestmentValueCalculator()
