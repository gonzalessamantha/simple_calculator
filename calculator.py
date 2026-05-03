import tkinter as tk

calculation = ()

def add_to_calc(symbol):
    pass

def evaluate_symbol(symbol):
    pass

def clear_field(symbol):
    pass

root = tk.Tk()
root.geometry("350x450")

text_result = tk.Text(root, width=20, height=2, font=("Arial", 24))
text_result.grid(columnspan=5)
root.mainloop()