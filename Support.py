
import random,os,time

import tkinter as tk

import tkinter.ttk as ttk

from tkinter import *

from PIL import ImageTk,Image



def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
    

def root_update():
    root.update()
    return

def root_destroy():
    root.destroy()
    return


class Toplevel1:

    def check(s,r, list1): #lows the plate selected in 4 player mode
        while(s>0):
            i=r-1
            if(s==list1[i]):
                list1[i]='-'
                s=s-r
                return s
            else: 
                s=s-r
                list1[i]='-'
                return s
    
    def toLow1(self, s,r, list1, list3):    #lows the plate selected in 2 player mode
        while(s>0):
            i=r-1
            if(s==list1[i]):
                list1[i]='-'
                list3[i]=s
                s=s-r
                return s
            else: 
                s=s-r
                list1[i]='-'
                list3[i]=r
                return s
    
    def toLow2(self, s,r, list2, list4):    #ups the plate selected in 2 player mode
        if s == int:
            while(s>0):
                i=r-1
                if(s==list4[i]):
                    list4[i]='-'
                    list2[i]=s
                    s=s-r
                    return s
                else: 
                    s=s-r
                    list4[i]='-'
                    list2[i]=r
                    return s
        
    def shut_box(self, list1):    #checks shut the box condition
        s2=0
        for i in list1:
            if(i!="-"):
               s2+=i
        if(s2==0):
            return True         
    
    def two_dice(self):     #gives sum of two dices
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        s=d1+d2
        return s
    
    def one_dice(self):     #gives sum of one dice
        d1=random.randint(1,6)
        s=d1  
        return s
    def ifSumExists(self, Sum,s,list1):   #checcks if sum exists in the list
        for i in list1:
                    if(i!='-'):
                        for x in list1:
                            if(x!='-'):
                                if(s==x):
                                    Sum=True
                                    return Sum
                                if(x!=i):
                                    sum2=i+x
                                    if(s==sum2):
                                        Sum=True
                                        return Sum
                                    for y in list1:
                                        if(y!=i):
                                            if(x!=y):
                                                if(y!='-'):
                                                    sum3=sum2+y
                                                    if(s==sum3):
                                                        Sum=True
                                                        return Sum
                                                    for z in list1:
                                                        if(z!=y):
                                                            if(x!=z):
                                                                if(z!=i):
                                                                    if(z!='-'):
                                                                        sum4=sum3+z
                                                                        if(s==sum4):
                                                                            Sum=True
                                                                            return Sum
    
    def getnumeric(self, lol):    #for exception handling
        while(True):
            response=input(lol)
            try:
                return int(response)
            except ValueError:
                print("please enter a number")
                           
    def getNum(self):
        return self.getnumeric("Which plate you want to lower: ")
    
        
    
    
    def modetwo(self, varb):
            
            Plates=[]
            
            ajeeb = 0 
            for i in range(2):
                list3=['-','-','-','-','-','-','-','-','-'] #list for player 2
                list1=[1,2,3,4,5,6,7,8,9]   #list for player 1
                while True:
                    while True:
                            Sum=False
                            list2=[]
                            list4=[]
                            for i in list1:
                                list2.append(i)
                            for i in list3:
                                list4.append(i)
                            print("It is player 1 turn") 
                            s=self.two_dice()
                            
                            self.Label3.configure(text='''Player 1's Turn''', font=("Courier", 20, "bold"))
                            root_update()
                            
                            time.sleep(2)
                            self.Label3.configure(text='''Player 1's Turn''', font=("Courier", 15, "bold"))
                            self.Label1.configure(text='''Player 1 :''', font=("Courier", 18, "bold"))

                            root_update()
        
                            print("You rolled :",s)
                            Sum=self.ifSumExists(Sum,s,list1)
                            print(Sum)
                            #time.sleep(5)
                            #input('Press ENTER to continue...')
                            #r=self.getnumeric("Which plate you want to lower: ")
                                                        
                            #r = await self.getNum()
                            
                            if(Sum):    
                                print("waiting...")
                                
                                self.showNumber( str(s)+".png")
                                
                                time.sleep(5)
                                self.Button6.wait_variable(varb)
                                root_update()
                                print("done waiting.")
                                #self.showNumber( str(s)+".png")
                                #root_update()
                            
                                low=int(self.Text3.get("1.0"))
                                while(low>4):
                                    low=int(self.Text3.get("1.0"))
                                Plates=[self.Text4, self.Text6, self.Text8, self.Text5, self.Text7, self.Text9]
                             
                                for i in range(low):
                                    while True:
                                        #r=self.getnumeric("Which plate you want to lower: ")
                                        r=int(Plates[i].get("1.0"))
                                        index=r-1
                                        if(not r>9):
                                            if(r==list1[index]):
                                                s=self.toLow1(s,r, list1, list3)
                                                break
                                            elif(r>s):
                                                print("plate value is not present sum")
                                                self.Button6.wait_variable(varb)
                                                root_update()
                            
                                            else:
                                                print("plate is not present to low")
                                                self.Button6.wait_variable(varb)
                                                root_update()
                            
                                
    
                                if(s==0):
                                    self.Text1.delete("1.0","end")
                                    strlist = "            [ "
                                    for eachEntry in list1:
                                        strlist+=str(eachEntry)+", "
                                    strlist=strlist[:-2]
                                    strlist+=" ]"
                                    self.Text1.insert(INSERT,strlist)
                                    root_update()
                                    print(list1)
                                if(s!=0):   
                                    self.Text1.delete("1.0","end")
                                    strlist = "            [ "
                                    for eachEntry in list2:
                                        strlist+=str(eachEntry)+", "
                                    strlist=strlist[:-2]
                                    strlist+=" ]"
                                    self.Text1.insert(INSERT,strlist)
                                    root_update()

                                    print(list2)
                                    print("Your turn is over.")
                                    
                                    
                                    self.Text1.delete("1.0","end")
                                    strlist = "            [ "
                                    for eachEntry in list4:
                                        strlist+=str(eachEntry)+", "
                                    strlist=strlist[:-2]
                                    strlist+=" ]"
                                    self.Text1.insert(INSERT,strlist)
                                    root_update()
                                    
                                    print(list4)
                                    break
                                if(self.shut_box(list1)):
                                    print("You have shut the box!!")
                                    print("Player 1 is winner!")
                                    self.Label3.configure(text='''Player 1 Won !''', font=("Courier", 20, "bold"))
                                    root_update()
                                    time.sleep(10)
                                
                                    root_destroy()
                                    break
                            else:
                                print("no sum")
                                print("Your turn is over.")
                                
                                self.Text1.delete("1.0","end")
                                strlist = "            [ "
                                for eachEntry in list4:
                                    strlist+=str(eachEntry)+", "
                                strlist=strlist[:-2]
                                strlist+=" ]"
                                self.Text1.insert(INSERT,strlist)
                                root_update()
                                Sum= True
                                    
                                print(list4)
                                break
                    if(self.shut_box(list1)):
                            break
        
                    while(True):  
                            Sum=False
                            list1=[]
                            for i in list2:
                                list1.append(i)
                            list3=[]
                            for i in list4:
                                list3.append(i)
                            
                            print("player 2 turn")
                            #print(list3)
                            
                            self.Label3.configure(text='''Player 2's Turn''', font=("Courier", 20, "bold"))
                            root_update()
                            
                            time.sleep(2)
                            self.Label3.configure(text='''Player 2's Turn''', font=("Courier", 15, "bold"))
                            
                            self.Label1.configure(text='''Player 2 :''', font=("Courier", 18, "bold"))
                            root_update()
                            
                            s1=self.two_dice()
                            print("You rolled :",s1)
                            Sum=self.ifSumExists(Sum,s1,list4)
                            if(Sum):    
                                print("waiting...")
                                
                                self.showNumber( str(s1)+".png")
                                
                                #Sum=self.ifSumExists(Sum,s1,list4)
            
                                time.sleep(5)
                                self.Button6.wait_variable(varb)
                                root_update()
                                print("done waiting.")
                                
                                #low=getnumeric("How many plates you want to up: ")
                                low=int(self.Text3.get("1.0"))
                                while(low>4):
                                    low=int(self.Text3.get("1.0"))
        
                                for i in range(low):
                                    while True:
                                    #    r=getnumeric("Which plate you want to up: ")
                                        r=int(Plates[i].get("1.0"))
                                        index=r-1
                                        if(not r>9):
                                            if(r==list4[index]):
                                                s1=self.toLow2(s1,r, list2, list4)
                                                break
                                            elif(r>s1):
                                                print("plate value is not present sum")
                                                self.Button6.wait_variable(varb)
                                                root_update()
                            
                                            else:
                                                print("plate is not present to low")
                                                self.Button6.wait_variable(varb)
                                                root_update()
                                if(s1==0):   
                                    print(list4)
                                    
                                    self.Text1.delete("1.0","end")
                                    strlist = "            [ "
                                    for eachEntry in list4:
                                        strlist+=str(eachEntry)+", "
                                    strlist=strlist[:-2]
                                    strlist+=" ]"
                                    self.Text1.insert(INSERT,strlist)
                                    root_update()
                                    
                                if(s1!=0):
                                    print(list3)
                                    
                                    self.Text1.delete("1.0","end")
                                    strlist = "            [ "
                                    for eachEntry in list3:
                                        strlist+=str(eachEntry)+", "
                                    strlist=strlist[:-2]
                                    strlist+=" ]"
                                    self.Text1.insert(INSERT,strlist)
                                    root_update()
                                    
                                    print("Your turn is over.")
                                    print(list1)
                                    
                                    
                                    self.Text1.delete("1.0","end")
                                    strlist = "            [ "
                                    for eachEntry in list1:
                                        strlist+=str(eachEntry)+", "
                                    strlist=strlist[:-2]
                                    strlist+=" ]"
                                    self.Text1.insert(INSERT,strlist)
                                    root_update()
                                    
                                    break
                                if(self.shut_box(list4)):
                                    print("You have shut the box!!")
                                    print("Player 2 is winner!")
                                    self.Label3.configure(text='''Player 2 Won !''', font=("Courier", 20, "bold"))
                                    root_update()
                                    time.sleep(10)
                                
                                    root_destroy()
                                    break
                                                
                            else:
                                print("no sum")
                                print("Your turn is over.")
                                print(list1)
                                
                                
                                self.Text1.delete("1.0","end")
                                strlist = "            [ "
                                for eachEntry in list1:
                                    strlist+=str(eachEntry)+", "
                                strlist=strlist[:-2]
                                strlist+=" ]"
                                self.Text1.insert(INSERT,strlist)
                                root_update()
                                    
                                break
                        
                    if(self.shut_box(list4)):
                            break
            
   
    
    def showNumber(self, imgname):
        imj= ImageTk.PhotoImage(Image.open(imgname))    
        self.Canvas1.create_image(0, 0, image=imj, anchor=NW)
        root_update()
        return
    
    def SetTrue(self):
        #cont=True
        return 
    
    
    
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
           
    
        varb = tk.IntVar()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
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

        top.geometry("1369x693+-6+1")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#212F3C")


        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.81, rely=0.13, relheight=0.420, relwidth=0.150)

        self.Canvas1.configure(background="#212F3C")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.088, rely=0.101, height=51, width=135)
        self.Label1.configure(background="#212F3C")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#F4D03F")
        self.Label1.configure(text='''Player 1 :''', font=("Courier", 18, "bold"))

#        self.Label2 = tk.Label(top)
#        self.Label2.place(relx=0.088, rely=0.303, height=51, width=135)
#        self.Label2.configure(background="#212F3C")
#        self.Label2.configure(disabledforeground="#a3a3a3")
#        self.Label2.configure(foreground="#F4D03F")
#        self.Label2.configure(text='''Player 2 :''', font=("Courier", 18, "bold"))

        self.Text1 = tk.Text(top, height=20, width=50)
        self.Text1.place(relx=0.205, rely=0.087, relheight=0.092, relwidth=0.53)
        self.Text1.configure(background="#F4D03F")
        self.Text1.configure(font=("TkTextFont", 30, 'bold'))
        self.Text1.configure(foreground="#212F3C")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")
        self.Text1.insert(INSERT,"            [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]")
#        self.Text1.insert(END,"[1,2, 3, 4, 5, 6, 7, 8, 9]")

#        self.Text2 = tk.Text(top)
#        self.Text2.place(relx=0.205, rely=0.289, relheight=0.091, relwidth=0.527)

#        self.Text2.configure(background="#F4D03F")
#        self.Text2.configure(font=("TkTextFont", 30, 'bold'))
#        self.Text2.configure(foreground="#212F3C")
#        self.Text2.configure(highlightbackground="#d9d9d9")
#        self.Text2.configure(highlightcolor="black")
#        self.Text2.configure(insertbackground="black")
#        self.Text2.configure(selectbackground="#c4c4c4")
#        self.Text2.configure(selectforeground="black")
#        self.Text2.configure(wrap="word")
#        self.Text2.insert(INSERT,"            [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.798, rely=0.736, height=81, width=244)
        self.Label3.configure(background="#212F3C")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#F4D03F")
        self.Label3.configure(text='''Player 1's Turn''', font=("Courier", 15, "bold"))

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.759, rely=0.043, relheight=0.908)
        self.TSeparator1.configure(orient="vertical")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.088, rely=0.405, height=38, width=366)
        self.TLabel1.configure(background="#212F3C")
        self.TLabel1.configure(foreground="#F4D03F")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''How Many Plates to Lower ?''', font=("Courier", 15, "bold"))

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.088, rely=0.707, height=39, width=356)
        self.TLabel2.configure(background="#212F3C")
        self.TLabel2.configure(foreground="#F4D03F")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Which Plates to Lower ?''', font=("Courier", 15, "bold"))

        self.Text3 = tk.Text(top)
        self.Text3.place(relx=0.438, rely=0.351, relheight=0.092, relwidth=0.054)

        self.Text3.configure(background="#F4D03F")
        self.Text3.configure(font=("TkTextFont", 30, 'bold'))
        self.Text3.configure(foreground="#212F3C")
        self.Text3.configure(highlightbackground="#d9d9d9")
        self.Text3.configure(highlightcolor="black")
        self.Text3.configure(insertbackground="black")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(selectforeground="black")
        self.Text3.configure(wrap="word")
        self.Text3.insert(INSERT,"0")

        self.Text4 = tk.Text(top)
        self.Text4.place(relx=0.438, rely=0.500, relheight=0.092, relwidth=0.047)

        self.Text4.configure(background="#F4D03F")
        self.Text4.configure(font=("TkTextFont", 30, 'bold'))
        self.Text4.configure(foreground="#212F3C")
        self.Text4.configure(highlightbackground="#d9d9d9")
        self.Text4.configure(highlightcolor="black")
        self.Text4.configure(insertbackground="black")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(selectforeground="black")
        self.Text4.configure(wrap="word")
        self.Text4.insert(INSERT,"0")


        self.Text5 = tk.Text(top)
        self.Text5.place(relx=0.438, rely=0.670, relheight=0.092, relwidth=0.047)

        self.Text5.configure(background="#F4D03F")
        self.Text5.configure(font=("TkTextFont", 30, 'bold'))
        self.Text5.configure(foreground="#212F3C")
        self.Text5.configure(highlightbackground="#d9d9d9")
        self.Text5.configure(highlightcolor="black")
        self.Text5.configure(insertbackground="black")
        self.Text5.configure(selectbackground="#c4c4c4")
        self.Text5.configure(selectforeground="black")
        self.Text5.configure(wrap="word")
        self.Text5.insert(INSERT,"0")


        self.Text6 = tk.Text(top)
        self.Text6.place(relx=0.519, rely=0.500, relheight=0.092, relwidth=0.047)

        self.Text6.configure(background="#F4D03F")
        self.Text6.configure(font=("TkTextFont", 30, 'bold'))
        self.Text6.configure(foreground="#212F3C")
        self.Text6.configure(highlightbackground="#d9d9d9")
        self.Text6.configure(highlightcolor="black")
        self.Text6.configure(insertbackground="black")
        self.Text6.configure(selectbackground="#c4c4c4")
        self.Text6.configure(selectforeground="black")
        self.Text6.configure(wrap="word")
        self.Text6.insert(INSERT,"0")


        self.Text7 = tk.Text(top)
        self.Text7.place(relx=0.519, rely=0.670, relheight=0.092, relwidth=0.047)

        self.Text7.configure(background="#F4D03F")
        self.Text7.configure(font=("TkTextFont", 30, 'bold'))
        self.Text7.configure(foreground="#212F3C")
        self.Text7.configure(highlightbackground="#d9d9d9")
        self.Text7.configure(highlightcolor="black")
        self.Text7.configure(insertbackground="black")
        self.Text7.configure(selectbackground="#c4c4c4")
        self.Text7.configure(selectforeground="black")
        self.Text7.configure(wrap="word")
        self.Text7.insert(INSERT,"0")

        self.Text8 = tk.Text(top)
        self.Text8.place(relx=0.599, rely=0.500, relheight=0.092, relwidth=0.047)

        self.Text8.configure(background="#F4D03F")
        self.Text8.configure(font=("TkTextFont", 30, 'bold'))
        self.Text8.configure(foreground="#212F3C")
        self.Text8.configure(highlightbackground="#d9d9d9")
        self.Text8.configure(highlightcolor="black")
        self.Text8.configure(insertbackground="black")
        self.Text8.configure(selectbackground="#c4c4c4")
        self.Text8.configure(selectforeground="black")
        self.Text8.configure(wrap="word")
        self.Text8.insert(INSERT,"0")


        self.Text9 = tk.Text(top)
        self.Text9.place(relx=0.599, rely=0.670, relheight=0.092, relwidth=0.047)

        self.Text9.configure(background="#F4D03F")
        self.Text9.configure(font=("TkTextFont", 30, 'bold'))
        self.Text9.configure(foreground="#212F3C")
        self.Text9.configure(highlightbackground="#d9d9d9")
        self.Text9.configure(highlightcolor="black")
        self.Text9.configure(insertbackground="black")
        self.Text9.configure(selectbackground="#c4c4c4")
        self.Text9.configure(selectforeground="black")
        self.Text9.configure(wrap="word")
        self.Text9.insert(INSERT,"0")
        
        
        self.Button5 = tk.Button(top, command= lambda: self.modetwo(varb))
        self.Button5.place(relx=0.835, rely=0.900, height=40, width=127)
        self.Button5.configure(activebackground="#B7950B")
        self.Button5.configure(activeforeground="#273746")
        self.Button5.configure(background="#F4D03F")
        self.Button5.configure(disabledforeground="#ABB2B9")
        self.Button5.configure(foreground="#212F3C")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Go !''', font=("Courier", 15, "bold"))


        self.Button6 = tk.Button(top, command=lambda: varb.set(1))
        self.Button6.place(relx=0.655, rely=0.900, height=40, width=127)
        self.Button6.configure(activebackground="#B7950B")
        self.Button6.configure(activeforeground="#273746")
        self.Button6.configure(background="#F4D03F")
        self.Button6.configure(disabledforeground="#ABB2B9")
        self.Button6.configure(foreground="#212F3C")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Cont''', font=("Courier", 15, "bold"))

if __name__ == '__main__':
    vp_start_gui()
    




