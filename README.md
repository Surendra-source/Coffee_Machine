# Coffee Machine Program – GitHub Project

## Project Overview

This project simulates a coffee machine using Python. The program allows users to order drinks, check available resources, process payments, and generate reports.

---

# Features

* Prompt users to select a drink:

  * Espresso
  * Latte
  * Cappuccino
* Turn off the machine using a secret keyword (`off`)
* Generate resource reports (`report`)
* Check if enough ingredients are available
* Process inserted coins
* Validate payment transactions
* Return change if extra money is inserted
* Deduct ingredients after successful purchase
* Keep track of total money earned

---

# Project Structure

```text
coffee-machine-project/
│
├── main.py
├── menu.py
├── resources.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Program Requirements

## 1. Prompt User

The machine continuously asks:

```python
What would you like? (espresso/latte/cappuccino):
```

After each completed action, the prompt appears again.

---

## 2. Turn Off Machine

Typing:

```python
off
```

will shut down the coffee machine.

---

## 3. Print Report

Typing:

```python
report
```

will display available resources.

Example:

```text
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

---

## 4. Check Resources

Before making a drink, the machine checks ingredient availability.

Example:

```text
Sorry there is not enough water.
```

---

## 5. Process Coins

The machine accepts:

* Quarters = $0.25
* Dimes = $0.10
* Nickels = $0.05
* Pennies = $0.01

Users enter the number of each coin.

Example:

```text
How many quarters?: 1
How many dimes?: 2
How many nickels?: 1
How many pennies?: 2
```

Calculation:

```text
0.25 + (0.10 × 2) + 0.05 + (0.01 × 2) = $0.52
```

---

## 6. Transaction Check

### Not Enough Money

If payment is insufficient:

```text
Sorry that's not enough money. Money refunded.
```

### Successful Transaction

If payment is successful:

* Drink is prepared
* Ingredients are deducted
* Profit increases
* Change is returned if needed

Example:

```text
Here is $0.50 in change.
Here is your latte ☕ Enjoy!
```

---

# Example Workflow

```text
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.00 in change.
Here is your latte ☕ Enjoy!
```

---

# Example Python Logic

```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
```

---

# How to Run

1. Install Python
2. Open terminal in project folder
3. Run:

```bash
python main.py
```

---

# GitHub Repository Setup

## Create Repository

1. Go to GitHub
2. Click **New Repository**
3. Name it:

```text
coffee-machine-project
```

4. Add README file
5. Upload project files

---

# Suggested Commit Messages

```text
Initial commit
Added coffee machine menu
Implemented resource checking
Added coin processing
Implemented transaction validation
Added reporting system
```

---

# Author

Surendra Bais

