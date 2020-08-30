import tkinter as tk


window = tk.Tk()
window.title('My second window')
window.geometry('500x300')

# 表单
e = tk.Entry(window, show=None)
e.pack()

#按钮函数
var = tk.StringVar()
def insert_point():
    var = e.get()
    t.insert('insert', var)
def insert_end():
    var = e.get()
    t.insert('end', var)

b1 = tk.Button(window, text='insert_point', command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert_end', command=insert_end)
b2.pack()
t = tk.Text(window, height=2)
t.pack()

tk.mainloop()