from tkinter import *
from tkinter import constants, ttk
from random import randint

class Dice:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._check = None
        self._button = None
        self.vars = []
        self.dice = []
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.vars.append(self.var1)
        self.vars.append(self.var2)
        self.vars.append(self.var3)
        self.vars.append(self.var4)
        self.vars.append(self.var5)

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def var_states(self):

        selected_dice = []
        unselected_dice = []

        if self.var1.get() != 0:
            selected_dice.append(self.dice[0])
        elif self.var1.get() == 0:
            unselected_dice.append(self.dice[0])

        if self.var2.get() != 0:
            selected_dice.append(self.dice[1])
        elif self.var1.get() == 0:
            unselected_dice.append(self.dice[1])

        if self.var3.get() != 0:
            selected_dice.append(self.dice[2])
        elif self.var1.get() == 0:
            unselected_dice.append(self.dice[2])

        if self.var4.get() != 0:
            selected_dice.append(self.dice[3])
        elif self.var1.get() == 0:
            unselected_dice.append(self.dice[3])

        if self.var5.get() != 0:
            selected_dice.append(self.dice[4])
        elif self.var1.get() == 0:
            unselected_dice.append(self.dice[4])

        self._frame.destroy()

        for i in range(len(selected_dice)): exec('Label%d=Label(self._root,text="You chose: %s")\nLabel%d.pack()' % (i,selected_dice[i],i))

    def show_dice(self, dice):  
        i = 0
        while i < len(dice):
            self._check = ttk.Checkbutton(self._frame, text=dice[i], variable=self.vars[i]).pack()
            i+=1
        self._button = ttk.Button(self._frame, text='I have chosen!', command=self.var_states).pack()

    def roll_dice(self, dice):
        self._frame = ttk.Frame(master=self._root)
        self._frame.pack(expand=True, fill=BOTH)

        new_dice = []
        self.dice = dice
        for die in self.dice:
            die = randint(1, 6)
            new_dice.append(die)
        self.dice = new_dice
        self.show_dice(new_dice)