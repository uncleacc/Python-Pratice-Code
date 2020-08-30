import tkinter as tk

window = tk.Tk()
window.title('my fourth window')
window.geometry('200x250')

L = tk.Label(window, width=20, height=2, bg='yellow', text='Empty')
L.pack()

def print_selection(val):
    L.config(text='You have selected ' + val)

S = tk.Scale(window, label='try me', from_=5, to=11, tickinterval=2, orient='horizontal', length=200, showvalue=1,
             resolution=0.1, command=print_selection)
S.pack()

window.mainloop()