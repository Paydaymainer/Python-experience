from tkinter import *
master = Tk()
from pycbrf import ExchangeRates, Banks

rates = ExchangeRates('2024-12-20', locale_en=True)
Lf1 = LabelFrame(master, text='Tenge', height= '20')
Etng = Entry(Lf1, width = '50', )
B = Button(master, text='Convert',width='36',height='2')
f1 = Frame(master)
f2 = Frame(master)
LfUSD = LabelFrame(f1, text='USD')
LfRUB = LabelFrame(f1, text='RUB')
LfEUR = LabelFrame(f2, text='EUR')
LfCHF = LabelFrame(f2, text='CHF')
lUSD = Label(LfUSD, text='0.0 $', width=20)
lRUB = Label(LfRUB, text='0.0 ₽', width=20)
lEUR = Label(LfEUR, text='0.0 €', width=20)
lCHF = Label(LfCHF, text='0.0 ₣', width=20)


def Convert():
    tng = (Etng.get())
    LfUSD = str(round(float(tng) / (float(rates['USD'].rate) / float(rates['KZT'].rate)), 2))+' $'
    LfRUB = str(round(float(tng) / (1/ float(rates['KZT'].rate)), 2))+' ₽'
    LfEUR = str(round(float(tng) / (float(rates['EUR'].rate) / float(rates['KZT'].rate)), 2))+' €'
    LfCHF = str(round(float(tng) / (float(rates['CHF'].rate) / float(rates['KZT'].rate)), 2))+' ₣'
    lUSD['text'] = LfUSD
    lRUB['text'] = LfRUB
    lEUR['text'] = LfEUR
    lCHF['text'] = LfCHF


B['command'] = Convert
Lf1.pack()
Etng.pack()
B.pack()
f1.pack()
f2.pack()
LfUSD.pack(side=LEFT)
LfRUB.pack(side=LEFT)
LfEUR.pack(side=LEFT)
LfCHF.pack(side=LEFT)
lUSD.pack()
lRUB.pack()
lEUR.pack()
lCHF.pack()

master.title("Currency exchange")
master.mainloop()