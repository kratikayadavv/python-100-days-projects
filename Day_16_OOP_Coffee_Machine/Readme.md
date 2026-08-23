# Coffee Machine

A simple command-line **Coffee Machine** program built in Python using **Object-Oriented Programming (OOP)** concepts.

The program allows users to order different types of coffee, checks whether enough resources are available, processes payments, and prepares the selected drink.

## Features

*  Choose from different coffee options
*  Accept and process payments
*  Generate a resource and money report
*  Check whether sufficient ingredients are available
*  Turn the machine off using the `off` command
*  Uses classes and objects to organize the program

## Technologies Used

* **Python**
* Object-Oriented Programming (OOP)
* Classes and Objects
* Modules and Imports
* Conditional Statements
* While Loops
* User Input

## Project Structure

Coffee-Machine/
│
├── main.py
├── menu.py
├── coffee_maker.py
└── money_machine.py


### File Description

* `main.py` — Controls the main coffee machine program.
* `menu.py` — Contains the coffee menu and drink-related functionality.
* `coffee_maker.py` — Handles ingredients, resources, and making coffee.
* `money_machine.py` — Handles payment and money-related operations.

## 💡 How It Works

The program creates objects from three main classes:

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


The user then selects a drink. The program:

1. Displays the available menu items.
2. Checks whether the selected drink exists.
3. Checks if enough ingredients are available.
4. Processes the user's payment.
5. Makes the coffee if both conditions are satisfied.

##  What I Learned

Through this project, I practiced:

* Creating and using Python classes
* Working with multiple modules
* Object-oriented programming
* Using methods from different classes
* Managing program flow with loops and conditions
* Building a small real-world command-line application

