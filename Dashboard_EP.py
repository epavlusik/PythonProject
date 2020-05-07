import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import os.path, time
import threading
import glob

root= tk.Tk()
root.title("Dashboard")

entry1 = tk.Entry (root)
entry2 = tk.Entry (root)
entrytask = tk.Entry (root)
projvyska = 350
projsirka = 70
env1pressed = 0
env1color = ""
env2pressed = 0
env2color = ""
env3pressed = 0
env3color = ""
env4pressed = 0
env4color = ""
env5pressed = 0
env5color = ""

env = []
env.extend([None]*5)  # Definujem si velkost pola, nedalo by sa hned referencovat
health = 0
everything = []
projects = []
pomocnaprojekt = ""
projektky = []
projektkydetail = []
pomocnatodos = ""
todos = []
longstring = ""
pocetprojektov = 0
pressed = 0    # Show more, show less
Ludia = []
Ludia.extend([None]*12)
#Dvajaludia = []
#Dvajaludia.extend([None]*2)

#-----------------------------------------------------------------------------------------
file = open("testdata.txt")      #Natiahnutie data
longstring = file.read()
#longstring = longstring.replace("4ÿþ","")
longstring = longstring.replace("&","")
everything = longstring.split('~')    
pomocnaprojekt = everything[1]
projektky = pomocnaprojekt.split('$')
pocetprojektov = len(projektky)
pomocnatodos = everything[2]
todos = pomocnatodos.split('$')

#----------------------------------------------------------------------------------

env[0] = longstring[0]
env[1] = longstring[1]
env[2] = longstring[2]
env[3] = longstring[3]
env[4] = longstring[4]

if env[0] == "x":
    env1pressed = 1
    env1color = "red"
    health = health + 1
if env[0] == "e":
    env1pressed = 0
    env1color = "green"
   
if env[1] == "x":
    env2pressed = 1
    env2color = "red"
    health = health + 1

if env[1] == "e":
    env2pressed = 0
    env2color = "green"
   
if env[2] == "x":
    env3pressed = 1
    env3color = "red"
    health = health + 1

if env[2] == "e":
    env3pressed = 0
    env3color = "green"

if env[3] == "x":
    env4pressed = 1
    env4color = "red"
    health = health + 1

if env[3] == "e":
    env4pressed = 0
    env4color = "green"

if env[4] == "x":
    env5pressed = 1
    env5color = "red"
    health = health + 1

if env[4] == "e":
    env5pressed = 0
    env5color = "green"

canvas1 = tk.Canvas(root, width = 1100, height = 600, background ='gray')
canvas1.pack()

entry1 = tk.Text(root,width = 12, height=1, font=("Purisa", 14))
btnw = canvas1.create_window(110, 520, window=entry1)

entry2 = tk.Text(root,height=5, width=40, font=("Purisa", 12))
btnw2 = canvas1.create_window(450, 530, window=entry2)



canvas1.itemconfigure(btnw, state='hidden')
canvas1.itemconfigure(btnw2, state='hidden')

variable = tk.StringVar(root)# dropdown
variable.set("Select") # default value

PEOPLE = ["Peer1", "Peer2", "Peer3", "Peer4", "Peer5", "Peer6","Peer7","Peer8","Peer9", "Peer10", "Peer11", "Peer12", "Peer13"]

w1 = tk.OptionMenu(root, variable, *PEOPLE)

variable2 = tk.StringVar(root)# dropdown
variable2.set("Select") # default value

w2 = tk.OptionMenu(root, variable2, *PEOPLE)

dropdownik1 = canvas1.create_window(750, 520, window=w1)
dropdownik2 = canvas1.create_window(750, 560, window=w2)
canvas1.itemconfigure(dropdownik1, state='hidden')
canvas1.itemconfigure(dropdownik2, state='hidden')

canvas1.create_line(0, 450, 1100, 450)  # Ciara na rozdelenie vizualne

#----------------------------------------------------------------------------
def Envhealth():    # Funkcia na zobrazenie zdravia environmentu
    if health == 0:
        canvas1.create_oval(25, 75, 50, 100, fill="green")
    if health == 1:
        canvas1.create_oval(25, 75, 50, 100, fill="yellow")
    if health > 1 and health < 4:
        canvas1.create_oval(25, 75, 50, 100, fill="orange")
    if health > 3:
        canvas1.create_oval(25, 75, 50, 100, fill="red")
Envhealth()
#----------------------------------------------------------------------
def savethis():   # Ked stlacis save
    global longstring
    global entry1
    global entry2
    try:
        messagebox.showinfo("Cool", "well you tried")
    except:
        messagebox.showinfo("Error", "Did not connect")
    messagebox.showinfo("info",str(entry1.get()))
    messagebox.showinfo("info",str(entry2.get("1.0",END)))
    projektkydetail = str(entry1.get()) + "%" + str(entry2.get("1.0",END))
    #projektky[number]
#--------------------------------------------------------------------

class Project():   # Trieda na uchovanie dat o projektoch
    def __init__ (self, locationx, locationy, heightdrop, widthdrop, color, proj, text,ludia1,ludia2):    # konstruktor
        self.locationx = locationx
        self.locationy = locationy
        self.heightdrop = heightdrop
        self.widthdrop = widthdrop
        self.color = color
        self.proj = proj
        self.text = text
        self.ludia1 = ludia1
        self.ludia2 = ludia2
   
 
    def newdrop(self):    # Vykresli sa a prida do pola
        project=canvas1.create_rectangle(self.locationx, self.locationy, self.locationx+ self.heightdrop, self.locationy + self.widthdrop, fill=self.color, tags="playproject")
        canvas1.create_text(self.locationx + 160, self.locationy + 10, text=self.proj, font=("Purisa", 12), fill='black')  # Tu pridat este taku logiku ze IF prve styri, if dalsie styri
        canvas1.create_text(self.locationx + 60, self.locationy + 25, text=self.text, font=("Purisa", 6), fill='black')
        canvas1.create_text(self.locationx + 300, self.locationy + 45, text=self.ludia1, font=("Purisa", 8), fill='red')
        canvas1.create_text(self.locationx + 300, self.locationy + 55, text=self.ludia2, font=("Purisa", 8), fill='red')
        projects.append(project)   #Tu ho pridavam do pola
 
#---------z tohto skusit urobit metodu kvoli refreshovaniu-------------------------
       
for i in range (4):
    Detail = projektky[i]
    projektkydetail = Detail.split('%')
    Ludia[i] = projektkydetail[2]
    Lenludia = str(Ludia[i])
    Dvajaludia = Lenludia.split('#')
    project = Project(projvyska, projsirka, 350, 70, "yellow",str(projektkydetail[0]),str(projektkydetail[1]),str(Dvajaludia[0]),str(Dvajaludia[1])) # Toto je ako operator New      
    projsirka = projsirka + 100
    project.newdrop()    #Tu sa to vykresli pre kazdu jednu
   
#def vykresli:    Ak bude viac projektov, tuto metodu na vykreslovanie a refresh bude treba
#-----------------------------------------------------------------------------------------
def printcoords(event):
    if event.x > 350 and event.x < 700:
        if event.y > 70 and event.y < 140:
            vybielenie()
            aktivnyedit(0)
            canvas1.itemconfig(projects[0], fill="pink")
        if event.y > 170 and event.y < 240:
            vybielenie()
            aktivnyedit(1)
            canvas1.itemconfig(projects[1], fill="pink")
        if event.y > 270 and event.y < 340:
            vybielenie()
            aktivnyedit(2)
            canvas1.itemconfig(projects[2], fill="pink")
        if event.y > 370 and event.y < 440:
            vybielenie()
            aktivnyedit(3)
            canvas1.itemconfig(projects[3], fill="pink")
#----------------------------------------------------------------------------------
def vybielenie():   # Mozno ak by sa tu do parametra dalo ze dalsie projekty tak by to bolo najlepsie
    for i in range (4):
        canvas1.itemconfig(projects[i], fill="yellow")

#----------PODOBNA METODKA NA DALSIE PROJEKTY--------------------------------

   
#-------------------------------------------------------------------------------           
def aktivnyedit(number):           # Superdolezite, tu zobrazi options na edit
    global entry1
    global entry2
    global variable
    global variable2
    global PEOPLE
    global Ludia
    entry1.delete('1.0', END)
    entry2.delete('1.0', END)
    canvas1.itemconfigure(btnw5, state='hidden')
    canvas1.itemconfigure(hide, state='normal')
    canvas1.itemconfigure(btnw, state='normal')
    canvas1.itemconfigure(btnw2, state='normal')
    canvas1.itemconfigure(btnw3, state='normal')
    canvas1.itemconfigure(dropdownik1, state='normal')
    canvas1.itemconfigure(dropdownik2, state='normal')
    Lenludia = str(Ludia[number])
    Dvajaludia = Lenludia.split('#')
    variable.set(Dvajaludia[0])
    variable2.set(Dvajaludia[1])
    canvas1.itemconfigure(removacperac1, state='normal')
    canvas1.itemconfigure(removacperac2, state='normal')
    Detail = projektky[number]
    projektkydetail = Detail.split('%')
    entry1.insert(END, str(projektkydetail[0]))
    entry2.insert(END, str(projektkydetail[1]))
    messagebox.showinfo("info", str(Ludia[number]))
    canvas1.itemconfigure(texticek1, state='normal')
    canvas1.itemconfigure(texticek2, state='normal')
    canvas1.itemconfigure(texticek3, state='normal')
   
#----------------------------------------------------------------------------------------

def pridanieprojektu():          # Ak sa user rozhodne pridat projekt
    global entry1
    global entry2
    global button1
    entry1 = tk.Text(root,width = 12, height=1, font=("Purisa", 14))
    entry2 = tk.Text(root,height=5, width=40, font=("Purisa", 12))
    canvas1.create_window(110, 520, window=entry1)
    canvas1.create_window(450, 530, window=entry2)
    canvas1.itemconfigure(texticek1, state='normal')
    canvas1.itemconfigure(texticek2, state='normal')
    canvas1.itemconfigure(texticek3, state='normal')
    canvas1.create_window(1000, 520, window=button1)
    canvas1.create_window(750, 520, window=w1)
    canvas1.create_window(750, 560, window=w2)

canvas1.bind("<Button 1>",printcoords)     # Tu si vzdy budem zistovat koordinanty

#-------------------------------------------------------------------------------
def clicked(*args):       # Metoda na kliknuty env1
    global env1pressed
    global health
    global env
    if env1pressed == 0:
        canvas1.itemconfig(playbutton, fill="red")
        canvas1.itemconfig(playtext, text="ENV1 X")
        env1pressed = 1
        env[0] = "x"
        health = health + 1
    elif env1pressed == 1:
        canvas1.itemconfig(playbutton, fill="green")
        canvas1.itemconfig(playtext, text="ENV1")
        env1pressed = 0
        env[0] = "e"
        health = health - 1
    Envhealth()
#--------------------------------------------------------------------------------------
def clicked2(*args):    # Metoda na kliknute env2
    global env2pressed
    global health
    if env2pressed == 0:
        canvas1.itemconfig(playbutton2, fill="red")
        canvas1.itemconfig(playtext2, text="ENV2 X")
        env2pressed = 1
        env[1] = "x"
        health = health + 1
    elif env2pressed == 1:
        canvas1.itemconfig(playbutton2, fill="green")
        canvas1.itemconfig(playtext2, text="ENV2")
        env2pressed = 0
        env[1] = "e"
        health = health - 1
    Envhealth()
#------------------------------------------------------------------------------------
def clicked3(*args):
    print("You are zero!")

def clicked4(*args):    # Metoda na DTV
    global env3pressed
    global health
    Envhealth()
    if env3pressed == 0:
        canvas1.itemconfig(playbutton3, fill="red")
        canvas1.itemconfig(playtext3, text="ENV3 X")
        env3pressed = 1
        env[2] = "x"
        health = health + 1
    elif env3pressed == 1:
        canvas1.itemconfig(playbutton3, fill="green")
        canvas1.itemconfig(playtext3, text="ENV3")
        env3pressed = 0
        env[2] = "e"
        health = health - 1
    Envhealth()
#-------------------------------------------------------------------------------------
     # Metoda na Horizon

def clicked5(*args):   
    global env4pressed
    global health
    Envhealth()
    if env4pressed == 0:
        canvas1.itemconfig(playbutton4, fill="red")
        canvas1.itemconfig(playtext4, text="ENV4 X")
        env4pressed = 1
        env[3] = "x"
        health = health + 1
    elif env4pressed == 1:
        canvas1.itemconfig(playbutton4, fill="green")
        canvas1.itemconfig(playtext4, text="ENV4")
        env4pressed = 0
        env[3] = "e"
        health = health - 1
    Envhealth()

#-----------------------------------------------------------------------------------


def clicked6(*args):  
    global env5pressed
    global health
    Envhealth()
    if env5pressed == 0:
        canvas1.itemconfig(playbutton5, fill="red")
        canvas1.itemconfig(playtext5, text="ENV5 X")
        env5pressed = 1
        env[4] = "x"
        health = health + 1
    elif env5pressed == 1:
        canvas1.itemconfig(playbutton5, fill="green")
        canvas1.itemconfig(playtext5, text="ENV5")
        env5pressed = 0
        env[4] = "e"
        health = health - 1
    Envhealth()

#---------------------------------------------------------------------------------

def on_close():
    global longstring
    global env
    close = messagebox.askokcancel("Close", "Would you like to close the program?")
    if close:
        longstring = longstring[5:]
        longstring = str(env[0]) + str(env[1]) + str(env[2]) + str(env[3])+ str(env[4]) + longstring
        file = open("testdata.txt", "w")  # Naloadovanie zo sharu do txt
        file.write(longstring)
        file.close()
        root.destroy()

#----------------------------------Show More--------------------------------------------

def showmore():
    global pressed
    messagebox.showinfo("Pressed", "Ok")
    if pressed == 0:
        pressed = 1
        buttonMore['text'] = "Show Previous"
    elif pressed == 1:
        buttonMore['text'] = "Show Next"
        pressed = 0

#------------------------Remove Project-------------------------------------------------

def removeproject():
    messagebox.showinfo("Todo", "Todo")


#---------------------PridanieTasku--------------------------------------------

def pridanietasku():
    if len(todos) > 8:
        messagebox.showinfo("Warning", "Maximal count of TODOs reached!")
    else:
        canvas1.itemconfigure(btnw, state='hidden')
        canvas1.itemconfigure(btnw2, state='hidden')
        canvas1.itemconfigure(btnw3, state='normal')
        canvas1.itemconfigure(btnw4, state='normal')
        canvas1.itemconfigure(btnw5, state='normal')
        canvas1.itemconfigure(texticek1, state='hidden')
        canvas1.itemconfigure(texticek2, state='hidden')
        canvas1.itemconfigure(texticek3, state='hidden')
        canvas1.itemconfigure(dropdownik1, state='hidden')
        canvas1.itemconfigure(dropdownik2, state='hidden')
        canvas1.itemconfigure(removacperac1, state='hidden')
        canvas1.itemconfigure(removacperac2, state='hidden')
        canvas1.itemconfigure(hide, state='normal')
       
       
       

#---------------Save Task--------------------------------------------------

def savetask():
    global entrytask
    if len(todos) > 8:
        messagebox.showinfo("Warning", "Maximal count of TODOs reached!")
    else:

        todos.append(str(entrytask.get("1.0",END)))
        entrytask.delete('1.0', END)

#---------HIDE ALL-------------------------------------------------------

def hideall():
    canvas1.itemconfigure(btnw, state='hidden')
    canvas1.itemconfigure(btnw2, state='hidden')
    canvas1.itemconfigure(btnw3, state='hidden')
    canvas1.itemconfigure(btnw4, state='hidden')
    canvas1.itemconfigure(btnw5, state='hidden')
    canvas1.itemconfigure(texticek1, state='hidden')
    canvas1.itemconfigure(texticek2, state='hidden')
    canvas1.itemconfigure(texticek3, state='hidden')
    canvas1.itemconfigure(hide, state='hidden')
    canvas1.itemconfigure(dropdownik1, state='hidden')
    canvas1.itemconfigure(dropdownik2, state='hidden')
    canvas1.itemconfigure(removacperac1, state='hidden')
    canvas1.itemconfigure(removacperac2, state='hidden')
   
   
#---------------------------vykreslenie obrazovky------------------------------------------

hideall = tk.Button(text='Hideall', command=hideall, bg="green", height = 2, width = 10)   # TLACIDLO SAVE
hide = canvas1.create_window(50, 580, window=hideall)
canvas1.itemconfigure(hide, state='hidden')
 
button1 = tk.Button(text='Save', command=savethis, bg="orange", height = 5, width = 20)   # TLACIDLO SAVE
btnw3 = canvas1.create_window(1000, 520, window=button1)
canvas1.itemconfigure(btnw3, state='hidden')

buttonsavetask = tk.Button(text='Save', command=savetask, bg="orange", height = 5, width = 20)
btnw4 = canvas1.create_window(1000, 520, window=buttonsavetask)
canvas1.itemconfigure(btnw4, state='hidden')

entrytask = tk.Text(root,height=5, width=40, font=("Purisa", 12))
btnw5 = canvas1.create_window(450, 530, window=entrytask)
canvas1.itemconfigure(btnw5, state='hidden')

buttonaddpr = tk.Button(text='Add Project', bg="orange", command=pridanieprojektu, height = 2, width = 10) # TOTO TU BUDE STALE VISIBLE
canvas1.create_window(590, 40, window=buttonaddpr)

buttonaddtask = tk.Button(text='Add Task', bg="orange", command=pridanietasku, height = 2, width = 10) # STALE VISIBLE
canvas1.create_window(950, 40, window=buttonaddtask)



texticek1 = canvas1.create_text(100, 470, text="Project Name:", font=("Purisa", 16), fill='black')
texticek2 = canvas1.create_text(350, 470, text="Notes:", font=("Purisa", 16), fill='black')
texticek3 = canvas1.create_text(730, 470, text="Responsible:", font=("Purisa", 16), fill='black')
canvas1.itemconfigure(texticek1, state='hidden')
canvas1.itemconfigure(texticek2, state='hidden')
canvas1.itemconfigure(texticek3, state='hidden')

buttonremovepr = tk.Button(text='Remove', command=removeproject, bg="pink", height = 2, width = 8)

buttonremovepr2 = tk.Button(text='Remove', command=removeproject, bg="pink", height = 2, width = 8)

removacperac1 = canvas1.create_window(850, 520, window=buttonremovepr)
removacperac2 = canvas1.create_window(670, 40, window=buttonremovepr2)

canvas1.itemconfigure(removacperac1, state='hidden')
canvas1.itemconfigure(removacperac2, state='hidden')

justtext = canvas1.create_text(160, 40, text="ENVIRONMENT:", font=("Papyrus", 15), fill='black')

justtext2 = canvas1.create_text(450, 40, text="PROJECTS:", font=("Papyrus", 15), fill='black')

justtext3 = canvas1.create_text(830, 40, text="TODOs:", font=("Papyrus", 15), fill='black')
 
playbutton = canvas1.create_rectangle(75, 75, 225, 120, fill=env1color, tags="playbutton")
playtext = canvas1.create_text(150, 100, text="ENV1", font=("Papyrus", 26), fill='black',tags="playbutton")

playbutton2 = canvas1.create_rectangle(75, 200, 225, 150, fill=env2color, tags="playbutton2")
playtext2 = canvas1.create_text(150, 180, text="ENV2", font=("Papyrus", 26), fill='black',tags="playbutton2")

playbutton3 = canvas1.create_rectangle(75, 230, 225, 280, fill=env3color, tags="playbutton3")
playtext3 = canvas1.create_text(150, 260, text="ENV3", font=("Papyrus", 26), fill='black',tags="playbutton3")


playbutton4 = canvas1.create_rectangle(75, 310, 225, 360, fill=env4color, tags="playbutton4")
playtext4 = canvas1.create_text(150, 340, text="ENV4", font=("Papyrus", 26), fill='black',tags="playbutton4")


playbutton5 = canvas1.create_rectangle(75, 390, 225, 440, fill=env5color, tags="playbutton5")
playtext5 = canvas1.create_text(150, 420, text="ENV5", font=("Papyrus", 26), fill='black',tags="playbutton5")

if pocetprojektov > 4:
    buttonMore = tk.Button(text='Show Next', bg="orange",command=showmore, height = 2, width = 10)
    canvas1.create_window(750, 420, window=buttonMore)
   


canvas1.tag_bind("playbutton","<Button-1>",clicked) # <BUTTON-1> je lava mys

canvas1.tag_bind("playbutton2","<Button-1>",clicked2)

canvas1.tag_bind("playbutton2","<Button-3>",clicked3) # <BUTTON-3> prava mys

canvas1.tag_bind("playbutton3","<Button-1>",clicked4)  

canvas1.tag_bind("playbutton4","<Button-1>",clicked5)

canvas1.tag_bind("playbutton5","<Button-1>",clicked6)

canvas1.pack()

root.protocol("WM_DELETE_WINDOW",  on_close)

root.mainloop()
