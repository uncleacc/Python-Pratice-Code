import tkinter as tk

window = tk.Tk()
window.title('my selection option')
window.geometry('200x250')

var = tk.StringVar()
L = tk.Label(window, bg='yellow', width=20, height=2, text='Empty')
L.pack()

def print_selection():
    L.config(text="You have selected " + var.get())

r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()

r2 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r2.pack()

window.mainloop()
