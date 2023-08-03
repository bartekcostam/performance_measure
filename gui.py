from tkinter import Tk, Label, Entry, Button, StringVar
from test import test_loading_speed

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Loading Speed Test")
        self.window.geometry("300x100")
        self.url = StringVar()


        Label(self.window, text="URL:").pack()
        Entry(self.window, textvariable=self.url).pack()
        Button(self.window, text="Start Test", command=self.start_test).pack()

    def start_test(self):
        # Call function from main.py to start the test
        test_loading_speed(self.url.get())

    def run(self):
        self.window.mainloop()
