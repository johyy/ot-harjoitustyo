from tkinter import ttk, messagebox
from tkinter import *
from turtle import *
import turtle


class IndexView:
    def __init__(self, root, handle_choose_player_view, handle_top_score_view):
        self._root = root
        self._handle_choose_player_view = handle_choose_player_view
        self._handle_top_score_view = handle_top_score_view

        self._root["bg"] = "black"
        self._frame = None
        turtle.Screen().bgcolor("black")
        pen = turtle.Turtle()

        pen.width(6)
        pen.speed(10)

        pen.color("Red")
        pen.pensize(10)
        pen.pendown()
        pen.right(110)
        pen.fd(125)
        pen.bk(65)
        pen.right(110)
        pen.fd(50)
        pen.right(140)

        pen.color("Yellow")
        pen.pensize(10)
        pen.penup()
        pen.fd(130)
        pen.pendown()
        pen.right(110)
        pen.fd(125)
        pen.bk(125)
        pen.right(320)
        pen.fd(125)
        pen.bk(70)
        pen.right(100)
        pen.fd(40)
        pen.right(180)

        pen.color("Green")
        pen.pensize(10)
        pen.penup()
        pen.fd(110)
        pen.right(90)
        pen.pendown()
        pen.fd(100)
        pen.bk(100)
        pen.left(90)
        pen.fd(40)
        pen.bk(80)

        pen.color("Blue")
        pen.pensize(10)
        pen.penup()
        pen.fd(120)
        pen.right(90)
        pen.pendown()
        pen.left(90)
        pen.fd(80)
        pen.right(130)
        pen.fd(120)
        pen.left(130)
        pen.fd(80)

        pen.color("Purple")
        pen.pensize(10)
        pen.penup()
        pen.fd(60)
        pen.pendown()
        pen.right(110)
        pen.bk(125)
        pen.fd(65)
        pen.right(110)
        pen.fd(50)
        pen.right(140)

        pen.color("White")
        pen.pensize(5)
        pen.penup()
        pen.left(140)
        pen.fd(200)
        pen.pendown()
        pen.right(150)
        pen.bk(80)
        pen.left(90)
        pen.bk(80)
        pen.left(90)
        pen.bk(80)
        pen.left(90)
        pen.bk(80)
        pen.right(45)
        pen.bk(40)
        pen.left(45)
        pen.fd(80)
        pen.right(45)
        pen.fd(40)
        pen.right(45)
        pen.penup()
        pen.fd(80)
        pen.right(90)
        pen.fd(80)
        pen.pendown()
        pen.right(45)
        pen.fd(40)
        pen.right(45)
        pen.fd(80)

        pen.width(2)
        pen.penup()
        pen.bk(20)
        pen.right(135)
        pen.fd(10)
        pen.dot()
        pen.fd(15)
        pen.dot()
        pen.right(45)
        pen.fd(40)
        pen.dot()
        pen.left(45)
        pen.bk(15)
        pen.dot()

        pen.right(45)
        pen.bk(60)
        pen.right(90)
        pen.bk(20)
        pen.dot()
        pen.right(15)
        pen.bk(55)
        pen.dot()

        pen.right(45)
        pen.bk(35)
        pen.left(90)
        pen.fd(35)
        pen.dot()

        pen.width(15)
        pen.color("Orange")
        pen.right(10)
        pen.fd(180)
        pen.left(90)
        pen.pendown()
        pen.circle(280)

        self._initialize()

    def _yatzybutton(self):
        messagebox.showinfo('Yatzyyy', 'Are you ready to play?')

    def _playbutton(self):
        self._frame.destroy()
        self._handle_choose_player_view()

    def _topscorebutton(self):
        self._frame.destroy()
        self._handle_top_score_view()

    def _initialize(self):

        self._frame = Frame(master=self._root, background='Black')
        self._frame.grid()

        yatzypic = PhotoImage(file="src/pictures/yatzypic.png")
        play = PhotoImage(file="src/pictures/play.png")
        top_score = PhotoImage(file="src/pictures/topscore.png")

        yatzy_button = ttk.Button(
            self._frame, image=yatzypic, command=self._yatzybutton)
        yatzy_button.grid(row=1, column=2)
        play_button = ttk.Button(
            self._frame, image=play, command=self._playbutton)
        play_button.grid(row=2, column=2)
        top_score_button = ttk.Button(
            self._frame, image=top_score, command=self._topscorebutton)
        top_score_button.grid(row=3, column=2)

        self._root.mainloop()
