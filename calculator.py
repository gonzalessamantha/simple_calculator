from steps import CalculatorSteps
import tkinter as tk
import math

class MaangasNaCalculator(CalculatorSteps):
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
            result = str(eval(self.calculation, {"__builtins__": {}, "math": math}))
            if result == result.rstrip('.0'):
                result = result.rstrip('.0')
            self.calculation = result
            self.update_display(self.calculation)
        except Exception as e:
            self.clear_field()
            self.update_display("Syntax Error")

    def clear_field(self):
        self.calculation = ""
        self.update_display("")

    def update_display(self, text):
        self.text_result.delete(1.0,tk.END)
        self.text_result.insert(1.0,text)

    def create_widgets(self):
        self.text_result = tk.Text(self, width=16, height=2, font=("Arial", 24))
        self.text_result.grid(columnspan=5, row=0, sticky="ew")

def main():
    root = tk.Tk()
    root.geometry("450x600")
    root.title("Simpleng calculator ng Maangas")

    calc = MaangasNaCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()