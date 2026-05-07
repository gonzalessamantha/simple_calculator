import tkinter as tk
import math

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
            print(f"Evaluating: {self.calculation}")
            result = str(eval(self.calculation, {"__builtins__": {}, "math": math}))
            if result == result.rstrip('.0'):
                result = result.rstrip('.0')

            self.calculation = result
            self.update_display(self.calculation)
        except Exception as e:
            print(f"Error: {e}")
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
        for i in range(10):
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
        self.grid_rowconfigure(7, weight=1)
        self.grid_columnconfigure(8, weight=1)
        self.add_scientific_buttons()

    def add_scientific_buttons(self):
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
    root.geometry("400x500")
    root.title("Simpleng calculator ng Maangas")

        # Choose calculator type
    calc = ScientificCalculator(root)  # Change to SimpleCalculator(root) for basic version

    root.mainloop()

if __name__ == "__main__":
    main()