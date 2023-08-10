import customtkinter as ctk
 
class messageBox:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Downloading...")
        self.window.geometry("300x200")

        #Label
        ctk.CTkLabel(self.window, text="Downloading...").pack()

        #Progress bar
        global progressbar
        self.progressbar = ctk.CTkProgressBar(master=self.window, mode="determinate", width=300, height=15)
        self.progressbar.pack(padx=10, pady=10, fill=ctk.X, anchor=ctk.CENTER)
        self.progressbar.set(0)

    def set_progressbar(self, value):
        self.progressbar.set(value)

    def run(self):
        if self.window.state != 'normal':
            self.window.mainloop()

    def close(self):
        self.window.destroy()
