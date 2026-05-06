import tkinter as tk
import math

calculation = ""

class MaangasNaCalculator(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.calculation = ""
        self.grid(column=0, row=0, sticky="nsew")
        self.create_widgets()

    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.update_display(self.calculation)

    def evaluate_symbol(self):
        try:
            print(self.calculation)
            result = str(eval(self.calculation))
            if result == result.rstrip('.0'):
                result = result.rstrip('.0')
            self.calculation = result
            sellf.update_display(self,calculation)
        except:
            self.clear_field()
            self.update_display("Syntax Error")

    def clear_field(self):
        self.calculation = ""
        self.update_display("")

    def update_display(self, text):
        self.text_result.delete(1.0,tk.END)
        self.text_result.insert(1.0,text)

    def create_widgets(self):
        for i in range(7):
            self.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)

        self.text_result = tk.Text(self, width=16, height=2, font=("Arial", 24))
        self.text_result.grid(columnspan=5, row=0, sticky="ew")

        # Number buttons using loop
        numbers = [
            ('1', 1, 2), ('2', 2, 2), ('3', 3, 2),
            ('4', 1, 3), ('5', 2, 3), ('6', 3, 3),
            ('7', 1, 4), ('8', 2, 4), ('9', 3, 4),
            ('0', 2, 5)
        ]

        for text, col, row in numbers:
            btn = tk.Button(self, text=text,
                            command=lambda t=text: self.add_to_calculation(t),
                            width=5, font=("Arial", 15))
            btn.grid(column=col, row=row, sticky="nsew", padx=2, pady=2)

        # Operator buttons
        operators = [
            ('+', 4, 2), ('-', 4, 3), ('×', 4, 4), ('÷', 4, 5)
        ]
        for display, col, row in operators:
            op = {'×': '*', '÷': '/'}.get(display, display)
            btn = tk.Button(self, text=display,
                            command=lambda o=op: self.add_to_calculation(o),
                            width=5, font=("Arial", 15))
            btn.grid(column=col, row=row, sticky="nsew", padx=2, pady=2)

        # Parentheses
        tk.Button(self, text="(", command=lambda: self.add_to_calculation('('),
                  width=5, font=("Arial", 15)).grid(column=1, row=5, sticky="nsew", padx=2, pady=2)
        tk.Button(self, text=")", command=lambda: self.add_to_calculation(')'),
                  width=5, font=("Arial", 15)).grid(column=3, row=5, sticky="nsew", padx=2, pady=2)

        # Control buttons
        tk.Button(self, text="C", command=self.clear_field,
                  width=12, font=("Arial", 15)).grid(column=1, row=6, columnspan=2, sticky="nsew", padx=2, pady=2)
        tk.Button(self, text="=", command=self.evaluate_symbol,
                  width=12, font=("Arial", 15)).grid(column=3, row=6, columnspan=2, sticky="nsew", padx=2, pady=2)

class ScientificCalculator(MaangasNaCalculator):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.add_scientific_buttons()

    def add_scientific_buttons(self):
            # Add scientific functions in row 7+
        sci_buttons = [
            ('sin', 0, 7), ('cos', 1, 7), ('tan', 2, 7),
            ('√', 3, 7), ('^', 4, 7), ('log', 0, 8)
        ]

        for text, col, row in sci_buttons:
            if text == '√':
                cmd = lambda: self.add_to_calculation('√')
            elif text == '^':
                cmd = lambda: self.add_to_calculation('**')
            elif text == 'sin':
                cmd = lambda: self.add_to_calculation('sin(')
            elif text == 'cos':
                cmd = lambda: self.add_to_calculation('cos(')
            elif text == 'tan':
                cmd = lambda: self.add_to_calculation('tan(')
            elif text == 'log':
                cmd = lambda: self.add_to_calculation('log10(')
            else:
                cmd = lambda t=text: self.add_to_calculation(t)

            btn = tk.Button(self, text=text, command=cmd,
                            width=5, font=("Arial", 12))
            btn.grid(column=col, row=row, sticky="nsew", padx=2, pady=2)

def main():
    root = tk.Tk()
    root.geometry("350x450")
    root.title("Simpleng calculator ng Maangas")

        # Choose calculator type
    calc = ScientificCalculator(root)  # Change to SimpleCalculator(root) for basic version

    root.mainloop()

if __name__ == "__main__":
    main()

#     root = tk.Tk()
#     root.geometry("300x285")
#     root.title("Simple Calculator ng mga Maaangas")
#
#     text_result = tk.Text(root, width=16, height=2, font=("Arial", 24))
#     text_result.grid(columnspan=5, row=0)
#
#     # buttons for the calculator
#     button_one = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 15))
#     button_one.grid(column=1, row=2)
#     button_two = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 15))
#     button_two.grid(column=2, row=2)
#     button_three = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 15))
#     button_three.grid(column=3, row=2)
#     button_four = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 15))
#     button_four.grid(column=1, row=3)
#     button_five = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 15))
#     button_five.grid(column=2, row=3)
#     button_six = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 15))
#     button_six.grid(column=3, row=3)
#     button_seven = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 15))
#     button_seven.grid(column=1, row=4)
#     button_eight = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 15))
#     button_eight.grid(column=2, row=4)
#     button_nine = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 15))
#     button_nine.grid(column=3, row=4)
#     button_zero = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 15))
#     button_zero.grid(column=2, row=5)
#     button_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 15))
#     button_plus.grid(column=4, row=2)
#     button_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 15))
#     button_minus.grid(column=4, row=3)
#     button_multiplication = tk.Button(root, text="×", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 15))
#     button_multiplication.grid(column=4, row=4)
#     button_division = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 15))
#     button_division.grid(column=4, row=5)
#     # adding brackets for the function PMDAS
#     button_open_paren = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 15))
#     button_open_paren.grid(column=1, row=5)
#     button_close_paren = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 15))
#     button_close_paren.grid(column=3, row=5)
#     # equal and clearing buttons
#     button_equal = tk.Button(root, text="=", command=lambda: evaluate_symbol(), width=12, font=("Arial", 15))
#     button_equal.grid(column=3, row=6, columnspan=2)
#     button_clear = tk.Button(root, text="C", command=clear_field, width=12, font=("Arial", 15))
#     button_clear.grid(column=1, row=6, columnspan=2)
#
#
# class ScientificCalculator(SimpleCalculator):
#     def __init__(self):
#         super().__init__()
#         self.add_scientific_buttons()
#
#     def add_scientific_buttons(self):
#         # Add sin, cos, tan, sqrt, etc.
#         pass
#
# root.mainloop()