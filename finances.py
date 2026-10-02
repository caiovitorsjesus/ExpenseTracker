import datetime

class finances:
    def __init__(self):
        self.expenses = {}
        self.next_id = 1


    def addExpense(self):
        description = input("Enter the name of the expense: ").strip()
        if not description:
            print("Description cannot be empty.")
            return

        try:
            amount = float(input("Enter the amount of the expense: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return

        expense_id = self.next_id
        self.expenses[expense_id] = {
            "date": datetime.date.today().isoformat(),
            "description": description,
            "amount": amount,
        }
        self.next_id += 1
        print(f"Expense added successfully (ID: {expense_id})")

    def updateExpense(self):
        try:
            expense_id = int(input("Enter the ID of the expense to update: "))
        except ValueError:
            print("ID must be a number.")
            return

        if expense_id not in self.expenses:
            print("Expense not found.")
            return

        description = input("Enter the new description: ").strip()
        if not description:
            print("Description cannot be empty.")
            return

        try:
            amount = float(input("Enter the new amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return

        self.expenses[expense_id]["description"] = description
        self.expenses[expense_id]["amount"] = amount
        print("Expense updated successfully.")

    def deleteExpense(self):
        try:
            expense_id = int(input("Enter the ID of the expense to delete: "))
        except ValueError:
            print("ID must be a number.")
            return

        if expense_id not in self.expenses:
            print("Expense not found.")
            return

        del self.expenses[expense_id]
        print("Expense deleted successfully.")

    def viewExpenses(self):
        if not self.expenses:
            print("You haven't recorded expenses")
            return  
        print("ID  Date        Description  Amount")
        for expense_id, expense in self.expenses.items():
            amount_format = f"${expense['amount']:.2f}"
            print(
                f"{expense_id:<3} {expense['date']}  "
                f"{expense['description']}  {amount_format:>10}"
                )
    
    def summaryExpenses(self):
        if not self.expenses:
            print("You haven't recorded expenses")
            return   
        totalExpenses = 0
        for expense in self.expenses.values():
            totalExpenses += expense['amount']
        print(f"Total expenses: ${totalExpenses}")

    def specificSummary(self):
        if not self.expenses:
            print("You haven't recorded expenses")
            return
        try:
            month = int(input("Month you want to filter (1-12): "))
        except ValueError:
            print("Month must be a number between 1 and 12.")
            return

        if not 1 <= month <= 12:
            print("Month must be a number between 1 and 12.")
            return

        current_year = datetime.date.today().year
        total_specific_expense = 0
        for expense in self.expenses.values():
            expense_date = datetime.date.fromisoformat(expense["date"])
            if expense_date.month == month and expense_date.year == current_year:
                total_specific_expense += expense["amount"]

        print(
            f"Total expenses for month {month} in {current_year}: "
            f"${total_specific_expense:.2f}"
        )
                 
