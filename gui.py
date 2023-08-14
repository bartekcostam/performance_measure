import customtkinter as ctk
from tkinter import StringVar, IntVar
from test import test_loading_speed

class GUI:
    def __init__(self, start_test, show_diagram):
        self.window = ctk.CTk()
        self.window.title("Loading Speed Test")
        self.window.geometry("800x600")
        self.url = StringVar()
        self.xpath = StringVar()
        self.headless_mode_var = IntVar()
        self.num_iterations = IntVar(value=5)  # Default value
        self.upload_speed = StringVar()
        self.download_speed = StringVar()

        # Create a CTkTabview
        self.tabview = ctk.CTkTabview(self.window)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)  # Fill the window

        # Add tabs
        tab1 = self.tabview.add("Basic")
        tab2 = self.tabview.add("Advanced")
        tab3 = self.tabview.add("Additional")

        # Right frame in tab1
        right_frame = ctk.CTkFrame(tab1)
        right_frame.pack(side="right", fill="both", expand=True)

        
        ctk.CTkLabel(right_frame, text="URL: (starts with protocol 'http', 'https')").pack()
        ctk.CTkEntry(right_frame, textvariable=self.url).pack()
        ctk.CTkLabel(right_frame, text="XPath of the element to wait for:").pack()
        ctk.CTkEntry(right_frame, textvariable=self.xpath).pack()
        ctk.CTkLabel(right_frame, text="Number of iterations:").pack()
        ctk.CTkEntry(right_frame, textvariable=self.num_iterations).pack()  # Entry for number of iterations

        # Checkbox for headless mode
        ctk.CTkCheckBox(right_frame, text="Run in headless mode", variable=self.headless_mode_var).pack(pady=20)

        ctk.CTkButton(right_frame, text="Start Test", command=start_test, width=200, height=30).pack(pady=0, padx=15)
        ctk.CTkButton(right_frame, text="Show Diagram", command=show_diagram, width=200, height=30).pack(pady=20,padx=15)

        # Left frame in tab1
        left_frame = ctk.CTkFrame(tab1)
        left_frame.pack(side="left", fill="both", expand=True)

        self.internet_speed_var = StringVar()

        ctk.CTkLabel(left_frame, text=" Internet Speed (Optional) ").pack()
        ctk.CTkRadioButton(left_frame, text="3G good", variable=self.internet_speed_var, value="3G good").pack(padx=5, pady=5)
        ctk.CTkRadioButton(left_frame, text="3G weak", variable=self.internet_speed_var, value="3G weak").pack(padx=5, pady=5)
        ctk.CTkRadioButton(left_frame, text="4G good", variable=self.internet_speed_var, value="4G good").pack(padx=5, pady=5)
        ctk.CTkRadioButton(left_frame, text="4G weak", variable=self.internet_speed_var, value="4G weak").pack(padx=5, pady=5)
        ctk.CTkLabel(left_frame, text="Upload Speed (Mbps):").pack()
        ctk.CTkEntry(left_frame, textvariable=self.upload_speed).pack()
        ctk.CTkLabel(left_frame, text="Download Speed (Mbps):").pack()
        ctk.CTkEntry(left_frame, textvariable=self.download_speed).pack()
        ctk.CTkLabel(left_frame, text="Latancy (ms):").pack()
        ctk.CTkEntry(left_frame, textvariable=self.download_speed).pack()

        # Labels for tab2 and tab3
        ctk.CTkLabel(tab2, text="Advanced").pack()
        ctk.CTkLabel(tab3, text="Additional").pack()

        

        # Information box
        global info_text
        self.info_text = StringVar()
        self.info_text.set("")
        ctk.CTkLabel(tab1, textvariable=self.info_text).pack(side='bottom')

        # Progress bar
        global progressbar
        self.progressbar = ctk.CTkProgressBar(master=tab1, mode="determinate", width=1000, height=10)
        self.progressbar.pack(side="bottom" ,padx=10, pady=20)
        self.progressbar.set(0)

    def set_infotext(self, text):
        self.info_text.set(text)

    def set_progressbar(self, value):
        self.progressbar.set(value)

    def run(self):
        self.window.mainloop()

    def is_headless_mode(self):
        return self.headless_mode_var.get() == 1

    def start_test(self):
        # Call function from main.py to start the test
        test_loading_speed(self.url.get())

    def get_num_iterations(self):
        return self.num_iterations.get()


    def get_selected_speed(self):
        selected_speed = self.internet_speed_var.get()
        if selected_speed:
            return selected_speed
        else:
            upload_speed = self.upload_speed.get()
            download_speed = self.download_speed.get()
        # Return these values to set the network conditions
        return upload_speed, download_speed
