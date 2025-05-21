import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from fpdf import FPDF
import os
import platform
import subprocess
from datetime import datetime

# Global variable
summary = ""

# Function to calculate rent and display summary
def calculate_rent():
    global summary
    try:
        rent = float(entry_rent.get())
        food = float(entry_food.get())
        electricity_spend = float(entry_units.get())
        charge_per_unit = float(entry_rate.get())
        persons = int(entry_persons.get())

        total_electricity = electricity_spend * charge_per_unit
        total = rent + food + total_electricity
        per_person = total / persons

        result_label.config(text=f"Each Person Pays: ₹{per_person:.2f}", fg="blue")

        summary = (
            f"Total Rent: ₹{rent:.2f}\n"
            f"Food Ordered: ₹{food:.2f}\n"
            f"Electricity Spend: {electricity_spend} units\n"
            f"Charge per Unit: ₹{charge_per_unit:.2f}\n"
            f"Total Electricity Bill: ₹{total_electricity:.2f}\n"
            f"Number of Persons: {persons}\n"
            f"------------------------------\n"
            f"Each Person Pays: ₹{per_person:.2f}"
        )

        text_summary.delete(1.0, tk.END)
        text_summary.insert(tk.END, summary)
        text_summary.pack(pady=10)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Reset all fields
def reset_fields():
    entry_rent.delete(0, tk.END)
    entry_food.delete(0, tk.END)
    entry_units.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_persons.delete(0, tk.END)
    result_label.config(text="")
    text_summary.delete(1.0, tk.END)

# GUI setup
root = tk.Tk()
root.title("RENT CALCULATOR")
root.geometry("550x600")
root.config(bg="#f0f8ff")

# Heading
tk.Label(root, text="RENT CALCULATOR", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#1e90ff").pack(pady=10)

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

# Input Fields
def labeled_entry(label_text):
    row = tk.Frame(frame, bg="#f0f8ff")
    tk.Label(row, text=label_text, width=25, anchor='w', bg="#f0f8ff").pack(side=tk.LEFT)
    entry = tk.Entry(row, width=25)
    entry.pack(side=tk.RIGHT)
    row.pack(pady=5)
    return entry

entry_rent = labeled_entry("Enter Rent (₹):")
entry_food = labeled_entry("Food Ordered (₹):")
entry_units = labeled_entry("Electricity Units Used:")
entry_rate = labeled_entry("Charge Per Unit (₹):")
entry_persons = labeled_entry("No. of Persons:")

# Buttons + Result
btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Calculate", command=calculate_rent, bg="green", fg="white", width=12).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Reset", command=reset_fields, bg="red", fg="white", width=12).grid(row=0, column=1, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue", bg="#f0f8ff")
result_label.pack(pady=10)

# Summary Text Box
text_summary = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD, font=("Arial", 10))

root.mainloop()
