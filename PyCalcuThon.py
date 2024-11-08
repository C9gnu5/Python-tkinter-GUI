from tkinter import *

mstr = Tk()

def add(): re.config(text="Sum:"), res.config(text=f"{int(txtF.get())+int(txtS.get())}")
def minus(): re.config(text="Difference:"), res.config(text=f"{int(txtF.get())-int(txtS.get())}")
def mult(): re.config(text="Product:"), res.config(text=f"{int(txtF.get())*int(txtS.get())}")
def div(): re.config(text="Quotient:"), res.config(text=f"{int(txtF.get())/int(txtS.get())}")
def intDiv(): re.config(text="Integer Quotient:"), res.config(text=f"{int(txtF.get())//int(txtS.get())}")
def expo(): re.config(text="Exponential:"), res.config(text=f"{int(txtF.get())**int(txtS.get())}")
def rem(): re.config(text="Remainder:"), res.config(text=f"{int(txtF.get())%int(txtS.get())}")
def clear(): txtF.delete(0, 'end'), txtS.delete(0, 'end'), res.config(text="0"), re.config(text="Result"), txtF.focus_set()

Label(mstr, text="PyCalcuThon", font=("Rockwell", 17, 'bold')).pack(side='top')
Label(mstr, text="First Number:", font=("Times New Roman", 14, 'bold')).place(relx=0.01, rely=0.085, anchor='nw')
Label(mstr, text="Second Number:", font=("Times New Roman", 14, 'bold')).place(relx=0.01, rely=0.18, anchor='nw')


txtF, txtS, res, re = Entry(mstr, font=("Times New Roman", 14, 'bold'), width=23), Entry(mstr, font=("Times New Roman", 14, 'bold'), width=23), Label(mstr, text="0", font=("Times New Roman", 20, 'bold')), Label(mstr, text="Result:", font=("Times New Roman", 20, 'bold'))
txtF.place(relx=0.37, rely=0.085, anchor='nw')
txtS.place(relx=0.37, rely=0.18, anchor='nw')
res.place(relx=0.55, rely=0.35, anchor='nw')
re.place(relx=0.01, rely=0.35, anchor='nw')

sign, com = ["+", "-", "*", "/", "//", "^x", "%", "C",], [add, minus, mult, div, intDiv, expo, rem, clear]
coor = [(0.06, 0.54), (0.28, 0.54), (0.06, 0.75), (0.28, 0.75), (0.5, 0.54), (0.72, 0.54), (0.5, 0.75), (0.72, 0.75)]
for i in range(len(sign)):
    for j in range(i+1):
        continue
    Button(mstr, text=sign[i], font=("Times New Roman", 30, 'bold'), width=3, bg='#DB8A00', command=com[i]).place(relx=coor[i][i-j], rely=coor[i][i-j-1])

mstr.geometry("400x400+455+180")
mstr.title("PyCalcuThon")
mstr.mainloop()
