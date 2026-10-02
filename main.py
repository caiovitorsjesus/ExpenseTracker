import finances

my_expense = finances.finances()

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Update expense")
    print("4. Delete expense")
    print("5. Summary of all expenses")
    print("6. Summary for a month")
    print("7. Exit")

    try: 
        choice = int(input("Choose an option: "))
        match choice:
            case 1:
                my_expense.addExpense()
            case 2:
                my_expense.viewExpenses()
            case 3:
                my_expense.updateExpense()
            case 4:
                my_expense.deleteExpense()
            case 5:
                my_expense.summaryExpenses()
            case 6:
                my_expense.specificSummary()
            case 7:
                break
            case _:
                print("Invalid option!")
    except ValueError:
        print("Invalid option! Choose between the options.")        

		