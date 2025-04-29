
# Example tkinter program
# only for reference

from tkinter import *

"""
TK_Window = Tk()
label = Label(TK_Window, text="this is a label")

#define events
def onClick():
    print("click")

button = Button(TK_Window, text="this is a button, click!", fg="green", command=onClick)

#push widgets onto the window
label.pack()
button.pack()


TK_Window.mainloop()"""


class ButtonEvent:
    def __init__(self, _text):
        self.window = Tk()
        self.button = Button(self.window, text=_text, command= self.onClick)
        self.label = Label(self.window, text="not clicked yet")
        #push widgets and create window

        self.button.pack()
        self.label.pack()
        self.window.mainloop()  # start window

    def onClick(self):
        #change label
        print("label changes")

event = ButtonEvent()
