import tkinter as tk

import tkinter.ttk as ttk

import Support

def vp_start_gui():

    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(rt):
    global w, w_win, root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def SwitchPages():
    root.destroy()
    Support.vp_start_gui()
    
    
    
class Toplevel1:
    
    
    
    def HighScore(self):
        file=open("Lol.txt","r")        #reads file
        for i in file:
            print(i)
        self.Label2.configure(text=i)
    

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#1C2833'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1364x696+-7+0")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#212F3C")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.235, rely=0.014, height=137, width=747)
        self.Label1.configure(background="#212F3C")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#F4D03F")
        self.Label1.configure(text='''Welcome to SHUT THE BOX !''')
        self.Label1.configure(font=("Courier", 30, "bold"))

        self.Button1 = tk.Button(top, command=SwitchPages)
        self.Button1.place(relx=0.346, rely=0.417, height=54, width=427)
        self.Button1.configure(activebackground="#B7950B")
        self.Button1.configure(activeforeground="#273746")
        self.Button1.configure(background="#F4D03F")
        self.Button1.configure(disabledforeground="#ABB2B9")
        self.Button1.configure(foreground="#212F3C")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Play for 2 Players''', font=("Courier", 20, "bold"))

        self.Button3 = tk.Button(top, command= lambda: self.HighScore())
        self.Button3.place(relx=0.411, rely=0.546, height=44, width=227)
        self.Button3.configure(activebackground="#B7950B")
        self.Button3.configure(activeforeground="#273746")
        self.Button3.configure(background="#F4D03F")
        self.Button3.configure(disabledforeground="#ABB2B9")
        self.Button3.configure(foreground="#212F3C")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Highscore !''', font=("Courier", 15, "bold"))

        self.Button4 = tk.Button(top, command= root.destroy )
        self.Button4.place(relx=0.455, rely=0.662, height=34, width=127)
        self.Button4.configure(activebackground="#B7950B")
        self.Button4.configure(activeforeground="#273746")
        self.Button4.configure(background="#F4D03F")
        self.Button4.configure(disabledforeground="#ABB2B9")
        self.Button4.configure(foreground="#212F3C")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Exit''', font=("Courier", 15, "bold"))

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.153, rely=0.216, relwidth=0.703)


        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.235, rely=0.750, height=137, width=747)
        self.Label2.configure(background="#212F3C")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#F4D03F")
        self.Label2.configure(font=("Courier", 10, "bold"))

if __name__ == '__main__':
    vp_start_gui()





