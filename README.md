# Expense Tracker

This project is a simple command-line expense tracker inspired by the challenge available at https://roadmap.sh/projects/expense-tracker.

It is designed to help users record and manage daily expenses in a simple way. Each expense is stored with an ID, a date generated automatically by the program, a description, and an amount.

## What this project does

- Add a new expense
- View all recorded expenses
- Update an expense by ID
- Delete an expense by ID
- Show the total expense amount
- Show the total for a specific month in the current year

## Requirements

- Python 3.10 or later
- No external libraries required

## How to run

Open a terminal in the project folder and run:

```bash
python main.py
```

On Windows, you can also run:

```powershell
py main.py
```

The app will display a menu with available actions. Choose an option and follow the prompts in the terminal.

## Storage

Expenses are currently kept in memory while the application is running. If the program is closed, the data is lost. This project is a beginner implementation and does not yet persist data to a file.

## Project reference

Project challenge: https://roadmap.sh/projects/expense-tracker
