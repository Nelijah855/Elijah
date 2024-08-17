import tkinter as tk

from tkinter import *

from tkinter.ttk import Progressbar,Checkbutton,Radiobutton,Scrollbar
from tkinter import Listbox,Canvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window=Tk()
icon="C:/Users/HP/ishops/icon.ico"
window.wm_maxsize(width=1500,height=900)
window.minsize(width=1000,height=900)
window.configure(background='red')
window.iconbitmap(bitmap=icon)

Progressbar(maximum=100,orient='horizontal',value=29,mode='determinate').grid(column=4,row=9)
scrollbar=Scrollbar(orient='vertical')
scrollbar.grid(column=4,row=8)

listbox=Listbox(background='green',highlightcolor='red')
listbox.config(yscrollcommand = scrollbar.set) 
scrollbar.config(command = listbox.yview)
entry=Entry(textvariable=StringVar)
entered=entry.get()

 
def plot_graph():
    # Create a figure and a set of subplots
    fig = Figure(figsize=(8, 6), dpi=72)
    ax = fig.add_subplot(111,frameon=False)
    
    
    # Sample data to plot
    x = ['14:00', '14:00']
    y = [25, 35]
    
    # Plotting the data
    ax.plot(x,y)

    x = ['12', '12:30']
    y = [10, 15]
    
    # Plotting the data
    ax.plot(x,y)
    
    ax.bar('12:00','12m',width=0.1)
    """
    ax.bar(1.5,10,bottom=[3],width=0.3)
    ax.bar(2.0,10,bottom=[3],width=0.3)
    ax.bar(2.5,10,bottom=[3],width=0.3)
    ax.bar(3.0,10,bottom=[3],width=0.3)
    ax.bar(3.5,10,bottom=[3],width=0.3)
    ax.bar(4.0,10,bottom=[3],width=0.3)
    ax.bar(4.5,10,bottom=[3],width=0.3)
    ax.bar(5.0,10,bottom=[3],width=0.3)
    ax.bar(5.5,10,bottom=[3],width=0.3)
    ax.bar(6.0,10,bottom=[3],width=0.3)
    """
    ax.axis(xmin='12:00',xmax='19:00',ymin='12M',ymax='20M')
    ax.set_title("financial market")
    ax.set_xlabel("time")
    ax.set_ylabel("volume")
    #ax.remove()
    # Embedding the figure in Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0,columnspan=1,rowspan=1)



# Creating a frame for the plot
plot_frame = Frame(window)

plot_frame.grid(row=0, column=0, padx=10, pady=10,columnspan=1,rowspan=1)


entry.grid(column=6,row=8)
def insert():
    
    #listbox.curselection()
    enter=entry.get()
    
    enter=enter+ str(window.size()[0]/2)
    listbox.insert('end' ,enter)
    

Button(text='add',background='yellow',command=insert).grid(column=7,row=8)

#Canvas().grid(column=5,row=7)
Scrollbar(orient='vertical').grid(column=9,row=9)
def fun():
    
    Label(text="select",background='blue').grid(column=8,row=9)
    listbox.insert('end' ,'elijah')
    listbox.insert('end' ,'timothy')
    listbox.insert('end' ,'golden')
    listbox.insert('end' ,'zion')
    listbox.insert('end' ,'aine')
    listbox.insert('end' ,'boy')
    listbox.insert('end' ,'reacheal')

def ope():
    for i in range(3):
        Button(text="opened",width=10,height=2,background=ls[i],foreground='white',command=buy).grid(column=i,row=2,columnspan=1,rowspan=1)


def but():
    Button(text="market",background='green',width=10,height=2,command=ope).grid(column=2,row=6,columnspan=1,rowspan=1)
    Button(text="buy",background='green',width=10,height=2,command=buy).grid(column=3,row=6,columnspan=1,rowspan=1)
    Button(text="sell",background='red',width=10,height=2,command=plot_graph).grid(column=4,row=6,columnspan=1,rowspan=1)
    Button(text="exit",background='red',width=10,height=2,command=ex).grid(column=4,row=7,columnspan=1,rowspan=1)
    Button(text="Goto",background='red',width=10,height=2,command=atom).grid(column=4,row=7,columnspan=1,rowspan=1)
    Canvas(background='red',height=100,width=100).grid(column=4,row=1,columnspan=1,rowspan=1)
def sold():
    Button(text="sold",width=10,height=2,background='green',foreground='white',command=but).grid(column=3,row=2,columnspan=1,rowspan=1)
sold()
def buy():
    Button(text="buy",width=10,height=2,background='green',foreground='white',command=close).grid(column=4,row=2,columnspan=1,rowspan=1)
def close():
    Button(text="closed",width=10,height=2,background='green',foreground='white',command=close).grid(column=6,row=2,columnspan=1,rowspan=1)

def atom():
    Button(text="atomics inc",width=10,height=2,background='green',foreground='white',command=close).grid(column=8,row=8,columnspan=1,rowspan=1)
    new_window = tk.Toplevel(window,background='red')
    new_window.title('trado')
    

def ex():
    import sys
    sys.exit()



def fund():
    Label(text='funded',background='red').grid(column=7,row=9)
Radiobutton(text='True',name='first',command=fund,value='true').grid(column=3,row=9)
first=Checkbutton(command=fun,text='google')
first.grid(column=1,row=9)

Checkbutton(command=ope,text='tesla').grid(column=2,row=9)
Checkbutton(command=close,text='apple').grid(column=1,row=10)
listbox.bind("<<ListSelection>>",func=fund,add='')
listbox.grid(column=3,row=8)



#window.after(100,close)
window.title('Trade inc')
ls=['green','blue','red']
    




print(plot_frame.size())
window.mainloop()