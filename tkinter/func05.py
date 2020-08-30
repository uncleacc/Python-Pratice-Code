import tkinter as tk

window = tk.Tk()
window.title('my third window')
window.geometry('200x250')

L = tk.Label(window, width=20, height=2, bg='yellow', font=('Arial',10), text='You don\'t like either')
L.pack()

def print_selection():
    if((var1.get()==1) & (var2.get()==1)):
        L.config(text='You are fond of both')
    elif((var1.get()==1) & (var2.get()==0)):
        L.config(text='You are fond of Python')
    elif((var1.get()==0) & (var2.get()==1)):
        L.config(text='You are fond of C++')
    else:
        L.config(text='You don\'t like either')

var1 = tk.IntVar()
var2 = tk.IntVar()
b1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
b1.pack()
b2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
b2.pack()

window.mainloop()