# Expense Tracker

A simple command-line application for recording and managing expenses. Each expense is assigned an ID and an automatic date, along with the description and amount entered by the user.

## Features

- Add an expense
- List recorded expenses
- Update an expense by ID
- Delete an expense by ID
- Validate descriptions and amounts

## Requirements

- Python 3.10 or later
- No external dependencies

## Running the application

Open a terminal in the project directory and run:

```bash
python main.py
```

On Windows, you can also run:

```powershell
py main.py
```

Choose an option from the menu and follow the prompts in the terminal. To exit, choose `5. Exit`.

## Storage

Expenses are stored in memory only while the application is running. All records are lost when the application exits.
