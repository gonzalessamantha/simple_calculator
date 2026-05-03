import tkinter as tk

calculation = ()

def add_to_calculation(symbol):
    global calculation
    calculation = calculation + symbol
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)

def evaluate_symbol(symbol):
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calculation)
    except ValueError:
        clear_field()
        text_result.insert(1.0, "Syntax Error")

def clear_field(symbol):
    global calculation
    calculation = ""
    text_result.delete(1.0, "END")

root = tk.Tk()
root.geometry("350x450")

text_result = tk.Text(root, width=20, height=2, font=("Arial", 24))
text_result.grid(columnspan=5)
root.mainloop()