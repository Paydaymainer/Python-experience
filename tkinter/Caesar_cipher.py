from tkinter import*
root=Tk()
E=Entry(root, width='20')
B=Button(root,text='cipher',width='18', height='1')
F=Frame(root)
L=Label(F,text='', width='20', height='2')
secret_key = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y', 'y':'z', 'z':'a', ',':';', '.':':', ' ':'*'}
def cipher():
    message = E.get()
    secret_message = ''
    for i in message:
        if i in secret_key:
            secret_message+=secret_key[i]
        else:
            secret_message+=i
    L['text']=secret_message
B['command']=cipher
E.pack()
B.pack()
F.pack()
L.pack()
root.mainloop()