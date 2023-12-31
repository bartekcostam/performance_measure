import customtkinter as ctk
from tkinter import StringVar, IntVar, Toplevel, Label,Text,font,Scrollbar,Button
from test import test_loading_speed
from sql_interpreter import sql_interpreter

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
        self.custom_code = ""
        

        
        #tab2 variables

        self.db_address = StringVar()
        self.db_name = StringVar()
        self.db_user = StringVar()
        self.db_pass = StringVar()
        self.db_type = StringVar()


        #tab2 variables 

        self.vpn_address = StringVar()
        self.vpn_user = StringVar()
        self.vpn_pass = StringVar()
        self.vpn_key = StringVar()
        

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
        ctk.CTkButton(right_frame, text="Additional Steps", command=self.open_code_input_window, width=200, height=30).pack(pady=20, padx=15)
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

        # Bottom frame for tab1
        bot_frame = ctk.CTkFrame(tab1)
        bot_frame.pack(side="bottom", fill="x", expand=False)

        # Information box
        global info_text
        self.info_text = StringVar()
        self.info_text.set("")
        ctk.CTkLabel(bot_frame, textvariable=self.info_text, width=500, height=40).pack(side="bottom")

        # Progress bar
        global progressbar
        self.progressbar = ctk.CTkProgressBar(master=bot_frame, mode="determinate", width=1000, height=10)
        self.progressbar.set(0)

        
        

        # Right frame in tab2
        advanced_right_frame = ctk.CTkFrame(tab2)
        advanced_right_frame.pack(side="right", fill="both", expand=True)
        ctk.CTkLabel(advanced_right_frame, text="VPN - settings",font=('Ubuntu Regular', 20)).pack()
        
        
        #Left frame for tab2

        advanced_left_frame = ctk.CTkFrame(tab2)
        advanced_left_frame.pack(side="left", fill="both", expand=True)
        ctk.CTkLabel(advanced_left_frame, text="Database settings",font=('Ubuntu Regular', 20)).pack()
        #db details
        ctk.CTkLabel(advanced_left_frame, text="Database ip/host name:").pack()
        ctk.CTkEntry(advanced_left_frame, textvariable=self.db_address).pack()

        ctk.CTkLabel(advanced_left_frame, text="Database name:").pack()
        ctk.CTkEntry(advanced_left_frame, textvariable=self.db_name).pack()

        ctk.CTkLabel(advanced_left_frame, text="Database username:").pack()
        ctk.CTkEntry(advanced_left_frame, textvariable=self.db_user).pack()

        ctk.CTkLabel(advanced_left_frame, text="Database password:").pack()
        ctk.CTkEntry(advanced_left_frame, textvariable=self.db_pass).pack()

        

        ctk.CTkLabel(advanced_left_frame, text=" Select DB type : ").pack(pady=20)
        ctk.CTkRadioButton(advanced_left_frame, text="Oracle DB", variable=self.db_type, value="Oracle DB").pack(padx=5, pady=5)
        ctk.CTkRadioButton(advanced_left_frame, text="MySQL", variable=self.db_type, value="MySQL").pack(padx=5, pady=5)
        ctk.CTkRadioButton(advanced_left_frame, text="MS SQL", variable=self.db_type, value="MS SQL").pack(padx=5, pady=5)
        ctk.CTkRadioButton(advanced_left_frame, text="Other", variable=self.db_type, value="Other").pack(padx=5, pady=5)

        #Right frame for tab2

        ctk.CTkLabel(advanced_right_frame, text="VPN server name").pack()
        ctk.CTkEntry(advanced_right_frame, textvariable=self.vpn_address).pack()

        ctk.CTkLabel(advanced_right_frame, text="VPN username:").pack()
        ctk.CTkEntry(advanced_right_frame, textvariable=self.vpn_user).pack()

        ctk.CTkLabel(advanced_right_frame, text="VPN password:").pack()
        ctk.CTkEntry(advanced_right_frame, textvariable=self.vpn_pass).pack()

        ctk.CTkLabel(advanced_right_frame, text="VPN key:").pack()
        ctk.CTkEntry(advanced_right_frame, textvariable=self.vpn_key).pack()

        ctk.CTkButton(advanced_right_frame, text="Load provided data", command='', width=200, height=30).pack(pady=30, padx=15)
        ctk.CTkButton(advanced_right_frame, text="SQL Interpreter", command=sql_interpreter, width=200, height=30).pack(pady=30, padx=15)
        # Tab 3 - Additional
        ctk.CTkLabel(tab3, text="Additional").pack()

        


    def set_infotext(self, text):
        self.info_text.set(text)

    def set_progressbar(self, value):
        self.progressbar.pack(side="bottom" ,padx=10, pady=20)
        self.progressbar.set(value)

    def run(self):
        self.window.mainloop()

    def is_headless_mode(self):
        return self.headless_mode_var.get() == 1

    def start_test(self):
        # Call function from main.py to start the test
        test_loading_speed(self.url.get())

    

    def open_code_input_window(self):
        print("Additional Steps button clicked.")
        code_window = Toplevel(self.window)
        code_window.title("Enter Python Code")
        
        # Set dark theme for the window
        code_window.configure(bg='black')
        
        # Replace ctk.CTkEntry with standard Tkinter Text for multi-line input
        code_text = Text(code_window, width=60, height=20, bg='black', fg='white', font=("Arial", 20),insertbackground='yellow', selectbackground='red')
        code_text.pack(side="left", fill="both", expand=True)
        
        # Add a scrollbar
        scrollbar = Scrollbar(code_window, command=code_text.yview)
        scrollbar.pack(side="right", fill="y")
        
        code_text.config(yscrollcommand=scrollbar.set)
        
        # Save button
        ctk.CTkButton(code_window, text="Save and Close", command=lambda: self.save_and_close(code_text, code_window)).pack(side="bottom")
        
        
        # Create a font
        hint_font = font.nametofont("TkDefaultFont").copy()
        hint_font.actual()
        hint_font.config(size=14)

        # Add hints
        hint_label = Label(code_window, text="Hints:", font=hint_font, bg='black', fg='white')
        hint_label.pack()

        hints = [
            "To find an element by ID: driver.find_element_by_id('element_id')",
            "To find an element by XPath: driver.find_element_by_xpath('//tag[@attribute=\"value\"]')",
            "To add sleep: time.sleep(seconds)",
            "To click an element: element.click()",
            "To find an element by class: driver.find_element_by_class_name('class_name')",
            "To find an element by CSS selector: driver.find_element_by_css_selector('css_selector')"
        ]

        hint_text = Text(code_window, height=10, width=50, wrap="word", font=hint_font, bg='black', fg='white')
        hint_text.pack()
        hint_text.insert("1.0", "\n".join(hints))
        hint_text.config(state="disabled")  # Make it read-only

        code_window.lift()


# Add this method in the GUI class to save the code
    def save_and_close(self, code_text, code_window):
        code = code_text.get("1.0", "end-1c")  # Get text from Text widget
        print(f"Saved code: {code}")  # Corrected this line
        self.custom_code = code
        code_window.destroy()  # Close the window
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
    

