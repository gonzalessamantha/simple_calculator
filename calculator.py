import tkinter as tk
from tkinter import messagebox, simpledialog
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

class CalculatorSteps(MaangasNaCalculator):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_step = 0
        self.operations = ""
        self.number_1 = 0
        self.number_2 = 0
        self.result = 0
    #WIDGETS
        self.step_display = None
        self.oper_buttons = []
        self.number_1_entry = None
        self.number_2_entry = None
        self.next_button = None
        self.calculate_button = None
        self.result_label = None
        self.try_again_button = None
        self.exit_button = None
        self.number_1_label = None
        self.number_2_label = None

        self.create_step_widget()
        self.show_step_1()

    def create_step_widget(self):
        for widget in self.winfo_children():
            widget.destroy()

            title = tk.Label(self, text="SIMPLE CALCULATOR", font=("Arial", 20, "bold"), bg='lightgray')
            title.grid(column=0, row=0, columnspan=2, pady=10)
            self.step_display = tk.Label(self, text="Choose Operation", font=("Arial", 16, "bold"), bg='lightblue', relief='ridge')
            self.step_display.grid(column=0, row=1, columnspan=4, pady=10, sticky="ew")

            operators = [("➕ ADD", "add", 2), ("➖ SUB", "sub", 2),
                   ("✖️ MUL", "mul", 3), ("➗ DIV", "div", 3)]
            self.oper_buttons = []
            for i, (text, op, row) in enumerate(operators):
                button = tk.Button(self, text=text, command=lambda o=op: self.select_operation(o),
                               font=("Arial", 12, "bold"), bg='#3498db', fg='white',
                               width=10, height=2, relief='raised')
                button.grid(column=row, rowspan=2, columnspan=4, pady=10)
                self.oper_buttons.append(button)

            self.number_1_label = tk.Label(self, text="ENTER FIRST NUMBER", font=("Arial", 14))
            self.number_1_entry = tk.Entry(self, font=("Arial", 16), width=12, justify="center")
            self.number_1_entry.bind("<Return>", lambda e: self.next_step())

            self.number_2_label = tk.Label(self, text="ENTER SECOND NUMBER", font=("Arial", 14))
            self.number_2_entry = tk.Entry(self, font=("Arial", 16), width=12, justify="center")
            self.number_2_entry.bind("<Return>", lambda e: self.calculate())

            self.next_button = tk.Button(self, text="NEXT STEP", command=self.next_step,
                                         bg='lightgreen', fg='darkgreen', font=("Arial", 12, "bold"), width=12)
            self.calculate_button = tk.Button(self, text="CALCULATE", command=self.calculate,
                                         bg='#e74c3c', fg='white', font=("Arial", 12, "bold"), width=12)

            self.result_label = tk.Label(self, text="", font=("Arial", 20, "bold"), bg='darkblue', fg="lightyellow")

            self.try_again_button = tk.Button(self, text="🔄TRY AGAIN", command=self.try_again,
                                         bg='#f39c12', fg='white', font=("Arial", 12, "bold"), width=12)
            self.exit_button = tk.Button(self, text="THANK YOU!", command=self.exit_app,
                                         bg='gray', fg='white', font=("Arial", 12, "bold"), width=12)

    def show_step_1(self):
        self.current_step = 0
        self.step_display.config(text="CHOOSE OPERATION")
        self.hide_all_step_widgets
        for button in self.oper_buttons:
            button.config(state="normal")

    def select_operation(self, operation):
        self.operations = operation
        operation_names ={"add": "➕ Addition", "sub": "➖ Subtraction",
                   "mul": "✖️ Multiplication", "div": "➗ Division"}
        self.step_display.config(text=operation_names[operation])
        self.show_step_2()

    def show_step_2(self):
        self.current_step = 1
        self.step_display.config(text="ENTER FIRST NUMBER")

        self.number_1_label.grid(column=0, row=4, columnspan=2, pady=5)
        self.number_1_entry.grid(column=0, row=5, columnspan=2, pady=5)
        self.next_button.grid(column=0, row=6, columnspan=2, pady=10)
        self.number_1_entry.delete(0, tk.END)
        self.number_1_entry.focus()

    def next_step(self):
        try:
            self.number_1 = float(self.number_1_entry.get())
            self.show_step_3()
        except ValueError:
            messagebox.showerror("ERROR", "Invalid Number!")

    def show_step_3(self):
        self.current_step = 2
        self.number_1_label.grid_remove()
        self.number_1_entry.grid_remove()
        self.next_button.grid_remove()

        self.step_display.config(text="ENTER SECOND NUMBER")
        self.number_2_label.grid(column=0, row=4, columnspan=2, pady=5)
        self.number_2_entry.grid(column=0, row=5, columnspan=2, pady=5)
        self.calculate_button.grid(column=0, row=6, columnspan=2, pady=10)

        self.number_2_entry.delete(0, tk.END)
        self.number_2_entry.focus()

    def calculate(self):
        try:
            self.number_2 = float(self.number_2_entry.get())
            if self.operations == "add": self.result = self.number_1 + self.number_2
            elif self.operations == "sub": self.result = self.number_1 - self.number_2
            elif self.operations == "mul": self.result = self.number_1 * self.number_2
            elif self.operations == "div": self.result = self.number_1 / self.number_2
                if abs(self.number_2) < 0.0001:
                    raise ZeroDivisionError("Cannot divide by zero -_-")
                self.result = self.result / self.number_2

            operator_symbol = {"add":"+","sub":"-","mul":"×","div":"÷"}
            result_text = f"{self.number_1} {operator_symbol[self.operations]} {self.number_2} = {self.result}"
            self.step_display.config(text=result_text)

            self.hide_all_step_widgets()
            self.result_label.config(text="RESULT: {self.result.3f}")
            self.try_again_button.grid(column=0, row=7, columnspan=4, pady=20)

            self.try_again_button.grid(column=0, row=8, pady=10)
            self.exit_button.grid(column=2, row=8, pady=10)

        except ZeroDivisionError as e:
            messagebox.showerror("ERROR",str(e))
            self.number_2_entry.focus()
        except ValueError:
            messagebox.showerror("ERROR", "Invalid Number!")

    def try_again(self):
        self.hide_all_step_widgets()
        self.show_step_100()

    def exit_app(self):
        messagebox.showinfo("EXIT", "Thank you for using this MAANGAS NA CALCU")
        self.quir()

def main():
    root = tk.Tk()
    root.geometry("400x500")
    root.title("Simpleng calculator ng Maangas")

    calc = CalculatorSteps(root)
    root.mainloop()

if __name__ == "__main__":
    main()