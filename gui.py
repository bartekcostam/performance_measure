import customtkinter as ctk
from tkinter import StringVar, IntVar
from test import test_loading_speed
import subprocess

class GUI:
    def __init__(self, start_test):
        self.window = ctk.CTk()
        self.window.title("Loading Speed Test")
        self.window.geometry("600x400")
        self.url = StringVar()
        self.xpath = StringVar()
        self.headless_mode_var = IntVar()
        self.num_iterations = IntVar(value=5)  # Default value
        self.upload_speed = StringVar()
        self.download_speed = StringVar()

        right_frame = ctk.CTkFrame(self.window)  # Create a frame to hold the right-side widgets
        right_frame.pack(side="right")  # Pack the frame to the right side of the window

        ctk.CTkLabel(right_frame, text="XPath of the element to wait for:").pack()
        ctk.CTkEntry(right_frame, textvariable=self.xpath).pack()
        ctk.CTkLabel(right_frame, text="URL: (starts with protocol 'http', 'https')").pack()
        ctk.CTkEntry(right_frame, textvariable=self.url).pack()
        ctk.CTkLabel(right_frame, text="Number of iterations:").pack()
        ctk.CTkEntry(right_frame, textvariable=self.num_iterations).pack()  # Entry for number of iterations

        # Checkbox for headless mode
        ctk.CTkCheckBox(right_frame, text="Run in headless mode", variable=self.headless_mode_var).pack()

        ctk.CTkButton(right_frame, text="Start Test", command=start_test, width=20, height=2).pack(pady=5)
        ctk.CTkButton(right_frame, text="Show Diagram", command=self.show_diagram, width=20, height=2).pack(pady=5)

        # Left frame
        left_frame = ctk.CTkFrame(self.window)
        left_frame.pack(side="left")

        ctk.CTkLabel(left_frame, text="Internet Speed").pack()
        ctk.CTkCheckBox(left_frame, text="Option 1").pack()
        ctk.CTkCheckBox(left_frame, text="Option 2").pack()
        ctk.CTkCheckBox(left_frame, text="Option 3").pack()
        ctk.CTkCheckBox(left_frame, text="Option 4").pack()
        ctk.CTkLabel(left_frame, text="Upload Speed (Mbps):").pack()
        ctk.CTkEntry(left_frame, textvariable=self.upload_speed).pack()
        ctk.CTkLabel(left_frame, text="Download Speed (Mbps):").pack()
        ctk.CTkEntry(left_frame, textvariable=self.download_speed).pack()


    def show_diagram(self):
        subprocess.run(["python3", "diagram.py"])

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