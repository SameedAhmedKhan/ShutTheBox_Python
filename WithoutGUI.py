#Shehzad Niaz , 2018-mc-73 , sec B
import random,os,time
def check(s,r): #lows the plate selected in 4 player mode
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

def toLow1(s,r):    #lows the plate selected in 2 player mode
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

def toLow2(s,r):    #ups the plate selected in 2 player mode
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

def shut_box(list1):    #checks shut the box condition
    s2=0
    for i in list1:
        if(i!="-"):
           s2+=i
    if(s2==0):
        return True         

def two_dice():     #gives sum of two dices
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    s=d1+d2
    return s

def one_dice():     #gives sum of one dice
    d1=random.randint(1,6)
    s=d1  
    return s
def ifSumExists(Sum,s,list1):   #checcks if sum exists in the list
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

def getnumeric(lol):    #for exception handling
    while(True):
        response=input(lol)
        try:
            return int(response)
        except ValueError:
            print("please enter a number")

#asking for mode 4 players or 2
print("WELCOME TO SHUT THE BOX")
time.sleep(1)
os.system("cls")
print("Select mode:")
repeat="r"
time.sleep(1)
os.system("cls")
score={}
win=0
count=0
s2=s1=0

while(repeat=="r" or repeat=="R"):
    file=open("Lol.txt","r")        #reads file
    for i in file:
        print(i)
    mode=getnumeric("How many players are playing? (2 or 4): ") #asks for mode

    time.sleep(1)
    os.system("cls")
    if(mode==4):  #for 4 players
        for j in range(1,5):    #for turns
            dice=True
            choice=2
            list1=[1,2,3,4,5,6,7,8,9]
            print("It is player "+str(j)+" turn")
            while True:
                Sum=False
                check1=True
                list2=[]
                for i in list1:
                    list2.append(i)
            
                for i in range(6,9,1):   
                    if( list1[i] != '-'):
                        check1=False
                        break
            
                if(dice):
                    if(check1):
                        choice=getnumeric("How many dices you want to use: ")
                        dice=False
                if(choice==2):
                    s=two_dice()
                else:
                    s=one_dice()

                print("You rolled :",s)
                Sum=ifSumExists(Sum,s,list1)
            
                if(Sum):    
                    low=getnumeric("How many plates you want to lower: ")
                    while(low>4):
                        low=getnumeric("How many plates you want to lower: ")

                    for i in range(low):
                        while True:
                            r=getnumeric("Which plate you want to lower: ")
                            index=r-1
                            if(not r>9):
                                if(r==list1[index]):
                                    s=check(s,r)
                                    break
                                elif(r>s):
                                    print("plate value is not present sum")
                                else:
                                    print("plate is not present to low")
                    if(s==0):   
                        print(list1)
                    if(s!=0):
                        print(list2)
                        print("Your turn is over.")
                    
            
                        for i in list2:
                            if(i!="-"):
                                s1+=i
                                s2=s1
                        print("Score of player "+str(j)+" is :",s1)
                        score["Player"+str(j)]=s1
                        s1=0
                        break
                else:
                    print("no sum")
                    print("Your turn is over.")
                    for i in list2:
                        if(i!="-"):
                            s1+=i
                            s2=s1
                    print("Score of player "+str(j)+" is :",s1)
                    score["Player"+str(j)]=s1
                    s1=0
                    break
            time.sleep(3)
            os.system("cls")
            if(shut_box(list1)):
                print("You have shut the box!!")
                print("Player "+str(j)+" is winner!")
                break
        print(score.values())   #stores the score of players
        win=min(score.values())
        print("Winner is",[k for k,v in score.items() if v==win]," with score",win)
        file=open("Lol.txt","w")
        file.write("The lowest score is")
        file.write(" ")
        file.write(str(win))
        file.write(" ")
        file.write(time.ctime())
        file.close()

    elif(mode==2):#for 2 players
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
                    s=two_dice()

                    print("You rolled :",s)
                    Sum=ifSumExists(Sum,s,list1)
                
                    if(Sum):    
                        low=getnumeric("How many plates you want to lower: ")
                        while(low>4):
                            low=getnumeric("How many plates you want to lower: ")

                        for i in range(low):
                            while True:
                                r=getnumeric("Which plate you want to lower: ")
                                index=r-1
                                if(not r>9):
                                    if(r==list1[index]):
                                        s=toLow1(s,r)
                                        break
                                    elif(r>s):
                                        print("plate value is not present sum")
                                    else:
                                        print("plate is not present to low")
                        if(s==0):   
                            print(list1)
                        if(s!=0):   
                            print(list2)
                            print("Your turn is over.")
                            print(list4)
                            break
                        if(shut_box(list1)):
                            print("You have shut the box!!")
                            print("Player 1 is winner!")
                            break
                    else:
                        print("no sum")
                        print("Your turn is over.")
                        print(list4)
                        break
                if(shut_box(list1)):
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
                    s1=two_dice()
                    print("You rolled :",s1)
                    Sum=ifSumExists(Sum,s1,list4)

                    if(Sum):    
                        low=getnumeric("How many plates you want to up: ")
                        while(low>4):
                            low=getnumeric("How many plates you want to up: ")

                        for i in range(low):
                            while True:
                                r=getnumeric("Which plate you want to up: ")
                                index=r-1
                                if(not r>9):
                                    if(r==list4[index]):
                                        s1=toLow2(s1,r)
                                        break
                                    elif(r>s1):
                                        print("plate value is not present sum")
                                    else:
                                        print("plate is not present to low")
                        if(s1==0):   
                            print(list4)
                        if(s1!=0):
                            print(list3)
                            print("Your turn is over.")
                            print(list1)
                            break
                        if(shut_box(list4)):
                            print("You have shut the box!!")
                            print("Player 2 is winner!")
                            break
                                        
                    else:
                        print("no sum")
                        print("Your turn is over.")
                        print(list1)
                        break
                
                if(shut_box(list4)):
                    break
    else:
        print("Only 2 or 4 players can play!")
    repeat=input("Enter R if you play again!")  #asking if he wants to play again
    while(repeat.isalpha()==False and count<2): #if user doesnot enters alphabet
        print("Enter alphabets only")
        repeat=input("Enter R if you play again: ")
        count+=1
print("You dont want to play more")
print("Goodbye")