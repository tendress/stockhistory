import tkinter as tk
from tkinter import messagebox

def calculate_final_value():
    try:
        current_account_value = float(entry_current_account_value.get())
        current_cash_value = float(entry_current_cash_value.get())
        raise_cash_amount = float(entry_raise_cash_amount.get())
        
        target_cash = current_account_value * 0.02
        if current_cash_value > target_cash:
            excess_cash = current_cash_value - target_cash
            messagebox.showinfo("Excess Cash", f"You have ${excess_cash:.2f} in your account")
        
        new_investable_cash = current_account_value - raise_cash_amount
        final_expected_value = current_account_value - raise_cash_amount + target_cash
        label_result.config(text=f"The final expected investable account value is: ${final_expected_value:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers (integer or decimal).")

# Create the main window
root = tk.Tk()
root.title("Final Cash Value Calculator")

# Create and place the input fields and labels
tk.Label(root, text="Enter the current account value:").grid(row=0, column=0, padx=10, pady=10)
entry_current_account_value = tk.Entry(root)
entry_current_account_value.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the current cash value:").grid(row=1, column=0, padx=10, pady=10)
entry_current_cash_value = tk.Entry(root)
entry_current_cash_value.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the amount of cash you want to raise:").grid(row=2, column=0, padx=10, pady=10)
entry_raise_cash_amount = tk.Entry(root)
entry_raise_cash_amount.grid(row=2, column=1, padx=10, pady=10)

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate_final_value)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create and place the result label
label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()