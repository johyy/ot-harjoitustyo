from tkinter import Tk
from ui.ui import UI

def main():
    root = Tk()
    root.title('Yatzy')

    ui = UI(root)
    ui.start()

    root.mainloop()

if __name__ == '__main__':
    main()