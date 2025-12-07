# 📊 Python Continuous Calculator (OOP & State Management)

An interactive command-line application designed to maintain a running total across multiple operations, demonstrating core concepts of **Object-Oriented Programming (OOP)** and modular file structure.

### ✨ Technical Highlights

* **State Management (OOP):** The application state (the running total) is managed exclusively by the **`ContinuousCalculator` class**. This class encapsulates the data (`self.result`) and methods (`calculate`, `clear`) that operate on it, reflecting the principle of encapsulation.
* **Modular Architecture:** The project separates concerns into dedicated files:
    * `continuous_calculator.py`: Manages the application state (the memory/result).
    * `calculator_functions.py`: Contains pure mathematical logic (e.g., `add`, `divide`).
    * `calculator.py`: Handles the user interaction loop and coordinates between the modules.
* **Dictionary Dispatch:** Mathematical functions are mapped to operator symbols (`+`, `-`, etc.) using a Python dictionary, allowing the program to execute the correct logic without relying on long, less efficient `if/elif` chains.
* **Robust Input Handling:** Custom functions handle user input validation, ensuring that only correct data types are passed to the calculation logic.

### 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [YOUR_GITHUB_URL_HERE]
    cd Calculator_Project
    ```
2.  **Execute the main script:**
    ```bash
    python calculator.py
    ```
    The application will launch an interactive loop, prompting you for an operator and a number.

### ⌨️ Available Commands

| Command | Action |
| :--- | :--- |
| `+`, `-`, `*`, `/` | Perform the calculation on the current total. |
| `c` | Clears the running total back to `0.0`. |
| `n` | Allows the user to set a **New** float value, overriding the current total. |
| `e` | Exits the application.
