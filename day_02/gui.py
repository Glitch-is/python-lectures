from tkinter import *

class App:
    def __init__(self, root):
        print(root)
        frame = Frame(root)
        frame.pack()

        self.button = Button(frame, text="Click me", fg="green", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_button = Button(frame, text="Hello", fg="blue", command=self.say_hello)
        self.hi_button.pack(side=LEFT)

    def say_hello(self):
        print("Hello")



root = Tk()

app = App(root)

root.mainloop()

