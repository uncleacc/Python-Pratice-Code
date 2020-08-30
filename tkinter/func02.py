import tkinter as tk

window = tk.Tk()
window.title('my third window')
window.geometry('500x250')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=8, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b.pack()

var2 = tk.StringVar()
var2.set((1, 2, 3, 4))
lb = tk.Listbox(window, listvariable=var2)
list_items = [5, 6, 7, 8]
for item in list_items:
    lb.insert('end',item)
lb.insert(0, 'first')
lb.insert(1, 'second')
lb.pack()

window.mainloop()
