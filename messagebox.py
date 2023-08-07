import customtkinter as ctk
 
class messageBox:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Downloading...")
        self.window.geometry("300x200")

    def run(self):
        self.window.mainloop()


