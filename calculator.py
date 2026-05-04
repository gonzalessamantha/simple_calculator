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
root.geometry("300x275")

text_result = tk.Text(root, width=16, height=2, font=("Arial", 24))
text_result.grid(columnspan=5)

# buttons for the calculator
button_one = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
button_one.grid(column=1, row=2)
button_two = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 15))
button_two.grid(column=2, row=2)
button_three = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 15))
button_three.grid(column=3, row=2)
button_four = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 15))
button_four.grid(column=1, row=3)
button_five = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 15))
button_five.grid(column=2, row=3)
button_six = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 15))
button_six.grid(column=3, row=3)
button_seven = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 15))
button_seven.grid(column=1, row=4)
button_eight = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 15))
button_eight.grid(column=2, row=4)
button_nine = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 15))
button_nine.grid(column=3, row=4)
button_zero = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 15))
button_zero.grid(column=2, row=5)
button_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 15))
button_plus.grid(column=4, row=2)
button_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 15))
button_minus.grid(column=4, row=3)
button_multiplication = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 15))
button_multiplication.grid(column=4, row=4)
button_division = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 15))
button_division.grid(column=4, row=5)


root.mainloop()