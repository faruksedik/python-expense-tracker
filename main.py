
# This script is created to test wheather the classes and methods are working correctly

from expense_tracker import Expense, ExpenseDatabase
from datetime import datetime

# Create an expense
expense1 = Expense("Groceries", 50.0)
expense2 = Expense("Utilities", 100.0)

# Create an expense database
db = ExpenseDatabase()

# Add expenses to the database
db.add_expense(expense1)
db.add_expense(expense2)

# Update an expense
expense1.update(title="Supermarket Groceries", amount=55.0)

# Remove an expense by ID
db.remove_expense(expense2.id)

# Retrieve an expense by ID
expense = db.get_expense_by_id(expense1.id)
print(expense.to_dict())

# Retrieve expenses by title
expenses = db.get_expense_by_title("Supermarket Groceries")
print([exp.to_dict() for exp in expenses])

# Convert all expenses to a dictionary
print(db.to_dict())