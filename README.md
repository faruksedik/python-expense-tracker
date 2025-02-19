
# Python Expense Tracker

## Author
- **Name: Faruk Sedik**


## Project Overview
The Python Expense Tracker is a simple yet effective application that demonstrates object-oriented programming (OOP) in Python. It models financial expenses using two primary classes:

- **Expense**: Represents an individual expense with attributes like a unique ID, title, amount, creation timestamp, and update timestamp. It also provides methods to update the expense details and convert the expense to a dictionary.
- **ExpenseDatabase**: Manages a collection of Expense objects. It supports adding, removing, and retrieving expenses (by ID or title) as well as outputting the complete list of expenses in a dictionary format.

In addition to these classes, the project includes an **__inity__.py** file to structure the project as a package and a **main.py** file that serves as the entry point for running the application.

This project is ideal for understanding how to structure Python code using classes and handling data in a clean, maintainable manner.

## Features
- **Unique Expense Identification**: Automatically generates a UUID for each expense.
- **Timestamp Management**: Automatically tracks creation and update times using UTC.
- **Easy Updates**: Allows users to modify the expense title and/or amount while updating the timestamp.
- **Expense Collection Management**: Offers functionalities to add, remove, and query expenses from a database.

## Prerequisites
- Python 3.x installed on your system.
- Basic knowledge of using the command line and Git.

## Getting Started

### Cloning the Repository and Running the Project
To get started with the project, clone the repository to your local machine:

1. Open your terminal or command prompt.
2. Run the following command:
   
   ```bash
   git clone https://github.com/faruksedik/python-expense-tracker.git

3. Navigate into the project directory:

   ```bash
   cd python-expense-tracker

4. Run the project using the following command:
   
   ```bash
   python main.py
