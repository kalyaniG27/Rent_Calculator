# 🏠 Rent Calculator (Tkinter)

A simple GUI-based Python application built using Python and Tkinter that helps multiple people living together easily calculate and split their shared monthly expenses. It is designed to streamline the often confusing and time-consuming task of determining how much each person owes.

🎯 Objective
To provide an intuitive and efficient tool that calculates individual contributions toward:

House Rent

Food Expenses

Electricity Bill
## 🚀 Features

- Calculate rent per person based on:
  - Total rent
  - Food expenses
  - Electricity usage and unit rate
  - Number of people sharing the rent
- View the detailed summary of all calculations
- Export summary as a **PDF**
- View last exported PDF directly
- Reset inputs easily

## 🖼️ UI Overview

- Clean and minimal Tkinter-based interface
- Color-coded buttons for better usability
- Scrollable text area for result summary

## 📦 Requirements

- Python 3.x
- `fpdf` library


🧮 How It Works

The total amount is calculated as:

Install dependencies using:

```bash
pip install fpdf

🧮 How It Works
The total amount is calculated as:

mathematica
Copy code
Total = Rent + Food + (Electricity Units × Rate per Unit)
Per Person = Total / Number of Persons

📁 File Structure
bash
Copy code
Rent_Calculator/
├── rent_calculator.py    # Main application file
├── README.md             # Project info and instructions
