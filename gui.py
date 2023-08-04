from tkinter import Tk, Label, Entry, Button, StringVar, IntVar, Checkbutton
from test import test_loading_speed
import subprocess

class GUI:
    def __init__(self, start_test):
        self.window = Tk()
        self.window.title("Loading Speed Test")
        self.window.geometry("400x300")
        self.url = StringVar()
        self.xpath = StringVar()
        
        self.headless_mode_var = IntVar()
        self.num_iterations = IntVar(value=5)  # Default value
        Label(self.window, text="Number of iterations:").pack()
        Entry(self.window, textvariable=self.num_iterations).pack()
        Label(self.window, text="XPath of the element to wait for:").pack()
        Entry(self.window, textvariable=self.xpath).pack()
        Label(self.window, text="URL: (starts with protocol 'http', 'https')").pack()
        Entry(self.window, textvariable=self.url).pack()

        # Checkbox for headless mode
        Checkbutton(self.window, text="Run in headless mode", variable=self.headless_mode_var).pack()

        Button(self.window, text="Start Test", command=start_test, width=20, height=2, bg="lightblue", font=("Helvetica", 12)).pack(pady=5)
        Button(self.window, text="Show Diagram", command=self.show_diagram, width=20, height=2, bg="lightgreen", font=("Helvetica", 12)).pack(pady=5)
        
    def show_diagram(self):
        subprocess.run(["python", "diagram.py"])

    def run(self):
        self.window.mainloop()

    def is_headless_mode(self):
        return self.headless_mode_var.get() == 1
    def start_test(self):
        # Call function from main.py to start the test
        test_loading_speed(self.url.get())

    def run(self):
        self.window.mainloop()

    def get_num_iterations(self):
        return self.num_iterations.get()