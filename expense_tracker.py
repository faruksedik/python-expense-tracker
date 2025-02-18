
import uuid
from datetime import datetime, timezone


class Expense:

    def __init__(self, title, amount):

        """
        Initialization of Expense instance with a unique ID, title, amount,
        and timestamps for creation and last update (both in UTC).
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = float(amount)
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    
    def update(self, title=None, amount=None):

        """
        This function will modifie the expense's title and/or amount, and any changes applied
        will result in the updated_at timestamp being reset to the current UTC time.
        """
        if title is not None:
            self.title = title

        if amount is not None:
            self.amount = float(amount)
        
        self.updated_at = datetime.now(timezone.utc)

        # I used this line "datetime.now(timezone.utc)" because datetime.utcnow() is deprecated
    
    def to_dict(self):

        """
        Returns a dictionary representation of the expense.
        """
        expence_dict = {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

        return expence_dict
    


class ExpenseDatabase:

    def __init__(self):
        
        """
        Initializes an ExpenseDatabase instance with an empty list to store expenses.
        """
        self.expenses = []

    
    def add_expense(self, expense):
       
        """
        Adds an Expense object to the database.
        """
        self.expenses.append(expense)


    def remove_expense(self, expense_id):
        
        """
        Removes an Expense object from the database.
        """
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    
    def get_expense_by_id(self, expense_id):
        
        """
        Retrieves an expense by its unique identifier (expense_id). Returns None if not found.
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    
    def get_expense_by_title(self, title):
        """
        Retrieves all expenses matching the provided title. Returns a list.
        """
        return [expense for expense in self.expenses if expense.title == title]

    
    def to_dict(self):
        """
        Returns a list of dictionaries representing each expense in the database.
        """
        return [expense.to_dict() for expense in self.expenses]

