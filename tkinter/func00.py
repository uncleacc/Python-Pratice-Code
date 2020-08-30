import tkinter as tk #导入tkinter模块

window = tk.Tk() #定义一个tk的窗口
window.title('my first window!!!') #定义窗口的标题
window.geometry('500x500') #定义窗口的尺寸

var = tk.StringVar() #字符串变量函数
label=tk.Label(window, textvariable=var, font=('Arial',15), bg='green', width=20, height=2,
               cursor='plus', fg='red') #显示窗口的标签
label.pack() #显示标签，函数还有place参数是坐标


on_click = False
def click_me():
    global on_click
    if(on_click == False):
        on_click = True
        var.set('You have clicked on me!')
    else:
        on_click = False
        var.set('')
b = tk.Button(window, text='Click on me', width=15, height=2, command=click_me) #按钮
b.pack()

window.mainloop() #必选项