# Getting Started with Python

Welcome to your first Python learning journey! This repository contains simple, beginner-friendly programs that help you understand core Python concepts step by step.

## 📚 Table of Contents
- [Why This Repository](#why-this-repository)
- [What You Need Before Starting](#what-you-need-before-starting)
- [How to Install Python](#how-to-install-python)
- [How to Run Python Programs](#how-to-run-python-programs)
- [Files in This Repository](#files-in-this-repository)
- [What Each Program Teaches](#what-each-program-teaches)
- [How to Learn Effectively](#how-to-learn-effectively)
- [Python Best Practices](#-python-best-practices)
- [Next Learning Goals](#-next-learning-goals)

## 🌟 Why This Repository
Python is a great language for beginners because it is easy to read and write. This repo is designed to help you practice real coding examples without overwhelming you.

## ✅ What You Need Before Starting
Make sure you have:
- Python installed on your computer
- A code editor such as VS Code, PyCharm, or IDLE
- A basic understanding of how to open files and use a terminal

> If you are new to coding, don't worry. You can learn by reading the code, running it, and making small changes.

## 🐍 How to Install Python
If you don't have Python installed on your machine, follow these steps:

### Windows
1. Go to [python.org](https://www.python.org/downloads/)
2. Click the **"Download Python"** button (it will download the latest version)
3. Run the installer executable file
4. **Important:** Check the box that says **"Add Python to PATH"** before clicking Install
5. Click **"Install Now"**
6. Wait for the installation to complete
7. Click **"Close"** when done

**Verify Installation:**
- Open Command Prompt (Press `Win + R`, type `cmd`, press Enter)
- Type: `python --version`
- You should see the Python version number (e.g., `Python 3.12.1`)

### macOS
1. Go to [python.org](https://www.python.org/downloads/)
2. Click the **"Download Python"** button for macOS
3. Run the installer package
4. Follow the installation wizard steps
5. When complete, Python will be installed

**Verify Installation:**
- Open Terminal (Press `Cmd + Space`, type `terminal`, press Enter)
- Type: `python3 --version`
- You should see the Python version number

### Linux (Ubuntu/Debian)
1. Open Terminal
2. Type the following command:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
3. Press Enter and wait for the installation to complete

**Verify Installation:**
- Type: `python3 --version`
- You should see the Python version number

### Troubleshooting
- **"python: command not found"** → Python may not be in your PATH. Try `python3` instead.
- **Still having issues?** → Reinstall Python and make sure to check "Add Python to PATH" (Windows only).

## ▶️ How to Run Python Programs
There are two common ways to run a Python file:

### Option 1: Using the Terminal
1. Open your terminal or command prompt.
2. Go to the project folder.
3. Run a script like this:
   ```bash
   python "Print_Function.py"
   ```
4. You can try another example as well:
   ```bash
   python "Arithmetic operations.py"
   ```

### Option 2: Using VS Code
1. Open the file in VS Code.
2. Click the Run button or use the Python extension.
3. Check the output in the terminal.

## 📁 Files in This Repository
```text
Getting-Started-with-Python/
├── Arithmetic operations.py
├── Bank_System.py
├── Count_Digita_Letters.py
├── ExampleFile.txt
├── Find even numvers from a range.py
├── Find in a String.py
├── Get Details from a Website.py
├── Numbers and Variables.py
├── Print_Function.py
├── Read From a File.py
├── Sort_Words_From_String.py
├── TemperatureConverter.py
├── Write in a File.py
├── downloaded_images/
└── README.md
```

## 🧠 What Each Program Teaches

### 1. `Print_Function.py`
This file teaches you how to use `print()` to show text and values on the screen.

### 2. `Numbers and Variables.py`
This file helps you understand variables, values, and how Python stores information.

### 3. `Arithmetic operations.py`
This file shows how to use operators like `+`, `-`, `*`, `/`, and `%` for calculations.

### 4. `Bank_System.py`
This file uses a simple banking menu with functions for withdraw, deposit, change PIN, and exit. It practices user input, conditions, and function calls.

### 5. `Count_Digita_Letters.py`
This file teaches you how to count letters and digits in a sentence or word.

### 6. `Find even numvers from a range.py`
This file shows how to check numbers in a range and print only the even ones.

### 7. `Find in a String.py`
This file teaches you how to use the `find()` method to search for characters or substrings within a text and get their positions (indices).

### 8. `Sort_Words_From_String.py`
This file teaches you how to split text into words and sort them.

### 9. `Get Details from a Website.py`
This file fetches a webpage, prints HTTP response details, shows HTML preview, and attempts to download image files.

### 10. `Read From a File.py`
This file explains how to open and read text from a file, read line by line, and parse CSV data.

### 11. `Write in a File.py`
This file shows how to write text to a new file and then read it back.

### 12. `TemperatureConverter.py`
This file teaches how to convert Celsius values to Fahrenheit using a math formula.

### 13. `ExampleFile.txt`
A sample text file used by `Read From a File.py` for practicing file reading.

### 14. `downloaded_images/`
A folder where images downloaded by `Get Details from a Website.py` are saved.

## 📖 How to Learn Effectively
Here is a simple way to study these files:
1. Read the code carefully.
2. Run the program and see the output.
3. Change one value and run it again.
4. Try to predict what the output will be before running it.
5. Write your own small example based on what you learned.

## ✨ Python Best Practices

### 1. Use Meaningful Variable Names
❌ **Bad:**
```python
x = 10
y = 20
z = x + y
```

✅ **Good:**
```python
age = 10
years_experience = 20
total_years = age + years_experience
```

### 2. Add Comments to Explain Your Code
```python
# Calculate the total years of experience
total_years = age + years_experience
print(f"Total years: {total_years}")
```

### 3. Use Constants for Fixed Values
```python
# Define constants in UPPERCASE
PI = 3.14159
MAX_USERS = 100
TAX_RATE = 0.08
```

### 4. Follow the PEP 8 Style Guide
- Use 4 spaces for indentation (not tabs)
- Keep lines under 79 characters
- Use lowercase with underscores for variable names: `user_name` instead of `userName`
- Use UPPERCASE for constants: `MAX_ATTEMPTS`

### 5. Keep Functions Simple and Focused
❌ **Bad:**
```python
def do_everything():
    # Read file, process data, save results - too much!
    pass
```

✅ **Good:**
```python
def read_user_data():
    # Only reads user data
    pass

def calculate_total(data):
    # Only calculates total
    pass

def save_results(results):
    # Only saves results
    pass
```

### 6. Always Close Files Using Context Manager
❌ **Bad:**
```python
file = open("data.txt", "r")
content = file.read()
file.close()  # Easy to forget!
```

✅ **Good:**
```python
with open("data.txt", "r") as file:
    content = file.read()
    # File automatically closes here
```

### 7. Handle Errors with Try-Except
```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number!")
```

### 8. Use Meaningful Function Names
- Function names should describe what they do
- Use verbs: `get_user_data()`, `calculate_total()`, `save_file()`
- Avoid: `process()`, `handle()`, `do_stuff()`

### 9. Don't Repeat Code - Use Loops and Functions
❌ **Bad:**
```python
print("Hello User 1")
print("Hello User 2")
print("Hello User 3")
```

✅ **Good:**
```python
users = ["User 1", "User 2", "User 3"]
for user in users:
    print(f"Hello {user}")
```

### 10. Write Code That's Easy to Read
- Avoid too many nested loops or conditions
- Break complex logic into smaller functions
- Use clear variable names instead of cryptic abbreviations
- Add whitespace to separate logical sections

### 11. Test Your Code
- Run your program with different inputs
- Check for edge cases (empty inputs, very large numbers, etc.)
- Make sure error handling works

### 12. Use Proper Naming Conventions
```python
# Classes use PascalCase
class BankAccount:
    pass

# Functions and variables use snake_case
def withdraw_money():
    pass

# Constants use UPPER_CASE
MAX_WITHDRAWAL = 5000
```

## 🚀 Next Learning Goals
After practicing these examples, you can move on to:
- `if`, `else`, and `elif`
- `for` and `while` loops
- Functions
- Lists and dictionaries
- Basic object-oriented programming
- Using Python modules

## 🎯 Final Tip
The best way to learn Python is by practicing every day, even if you only work on one small program at a time.

