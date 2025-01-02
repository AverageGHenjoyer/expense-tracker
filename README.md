# Expense Tracker

A command-line expense tracking application that helps you monitor and analyze your spending. Track expenses by
category, generate summaries, and export data to CSV.

## Features

- Add expenses with descriptions and categories
- List all expenses or filter by category
- Update existing expenses
- Delete expenses
- Generate monthly spending summaries
- Export data to CSV
- Categories include: Housing, Food, Transportation, Utilities, and more

## Requirements

- Python 3.10 or higher
- Required packages:
    - tabulate
    - pandas
    - json (built-in)

## Installation:

Clone the repo:

```bash
git clone https://github.com/maciej3j/expense-tracker.git
```

Get into cloned repo

```bash
cd expense-tracker
```
Create and Activate a Virtual Environment
```
python -m venv venv

# On Windows:
.\venv\Scripts\activate

# On macOS and Linux:
source venv/bin/activate
```
Install locally using pip

```bash
pip install -e .
```

Add to PATH

### Windows

1. Manual method:
    - Press Win + X and select "System"
    - Click "Advanced system settings"
    - Click "Environment Variables"
    - Under "User variables", find and select "Path"
    - Click "Edit"
    - Click "New"
    - Add the path to your expense-tracker directory
    - Click "OK" to close all windows

2. Command line method (run as administrator):

```bash
setx PATH "%PATH%;C:\path\to\expense-tracker"
```

Linux/Unix

1. For Bash

```bash
export PATH=$PATH:/path/to/expense-tracker
```

2. For Zsh

```bash
export PATH=$PATH:/path/to/expense-tracker
```

```markdown
## Usage

### Add an expense

```bash
expense-tracker add -a AMOUNT -d DESCRIPTION
# Example:
expense-tracker add -a 49.99 -d "Groceries from Walmart"
```

### List expenses

```bash
# List all expenses
expense-tracker list

# Filter by category
expense-tracker list -c "Food"
```

### Update an expense

```bash
expense-tracker update -id ID -a AMOUNT -d DESCRIPTION
# Example:
expense-tracker update -id 1 -a 52.99 -d "Updated description"
```

### Delete an expense

```bash
expense-tracker delete -id ID
# Example:
expense-tracker delete -id 1
```

### Get expense summary

```bash
# Get total expenses
expense-tracker summary

# Get expenses for specific month
expense-tracker summary -m 5  # For May
```

### Export to CSV

```bash
expense-tracker to_csv
```

## Categories

1. Mortgage or rent
2. Food
3. Transportation
4. Utilities
5. Subscriptions
6. Personal expenses
7. Savings and investments
8. Debt or student loan payments
9. Health care
10. Miscellaneous expenses
0. Other

## Data Storage

The application stores all expenses in a `data.json` file in the following format:

```json
{
  "ID": 1,
  "description": "Groceries",
  "amount": 49.99,
  "category": "Food",
  "created_at": "2025-01-01 15:14:00",
  "updated_at": "2025-01-01 15:14:00"
}
```

## Error Handling

- The application validates input data and provides appropriate error messages
- Negative amounts are not allowed
- Invalid category numbers will be marked as "Uncategorized"
- File not found errors are handled gracefully

