import customtkinter as ctk

def sql_interpreter():
    dialog = ctk.CTkInputDialog(text="Enter SQL query", title="SQL Interpreter")
    print("Recived SQL query: " + dialog.result)