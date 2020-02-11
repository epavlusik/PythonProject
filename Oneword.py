from tkinter import *

global Joker
global Ares
Joker = 0
Ares = 0
counter = 0
global listofwords
listofwords = [100]
file = open("bobor.txt", "r")
filee = file.read()
for x in range(len(filee)):
    if str(filee[x]) == ' ' or str(filee[x]) == '.' or str(filee[x]) == ',' or str(filee[x]) == '!'or str(filee[x]) == '?':
        counter = counter + 1
        listofwords.append(0)
    else:
        listofwords[counter] = str(listofwords[counter]) + str(filee[x])


# Window, and inheriting from the Frame
# Frame is a class from the tkinter module
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("ONE WORD")
        self.pack(fill=BOTH, expand=1)
        mumubutton = Button(self, text="-->",command=self.printword)
        mumubutton.place(x=20, y=40)
        skipbutton = Button(self, text="JUMP",command=self.jump)
        skipbutton.place(x=50, y=40)

    def jump(self):
        global Joker
        if(Joker + 20 < len(listofwords)):
            Joker = Joker + 20

    def printword(self):
        global Joker
        global Ares
        if(Joker < len(listofwords) - 3):
            Joker = Joker + 1
            Ares = Ares + 1
            if(Ares == 2):
                Ares = 1
                list = self.grid_slaves()
                for l in list:
                    l.destroy()
            else:
                Joker = 1
        darius = str(listofwords[Joker])
        darius = darius.replace("0","")
        darius = darius.replace("&","")
        darius = darius.replace(" ","")
        darius = darius.replace(" ","")
        darius = darius.replace(" ","")
        if len(darius) < 3:
            darius = "-->"
            text = Label(self, text= "  " + darius + "  ")
            text.config(font=("Courier", 18))
            text.grid(column=2, row=2)
root = Tk()
root.geometry("300x70")
app = Window(root)
root.mainloop()
