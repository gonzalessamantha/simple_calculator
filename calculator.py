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

# buttons for the calculator
button_one = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_one.grid(column=1, row=2)
button_two = tk.Button(root, text="2", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_two.grid(column=2, row=2)
button_three = tk.Button(root, text="3", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_three.grid(column=3, row=2)
button_four = tk.Button(root, text="4", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_four.grid(column=1, row=3)
button_five = tk.Button(root, text="5", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_five.grid(column=2, row=3)
button_six = tk.Button(root, text="6", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_six.grid(column=3, row=3)
button_seven = tk.Button(root, text="7", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_seven.grid(column=1, row=4)
button_eight = tk.Button(root, text="8", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_eight.grid(column=2, row=4)
button_nine = tk.Button(root, text="9", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_nine.grid(column=3, row=4)
button_zero = tk.Button(root, text="0", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_zero.grid(column=1, row=5)
root.mainloop()