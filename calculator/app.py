import customtkinter as ctk
ctk.set_appearance_mode("dark")


class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x520")
        self.resizable(False, False)
        