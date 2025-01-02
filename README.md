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

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

### Add an expense

```bash
python main.py add -a AMOUNT -d DESCRIPTION
# Example:
python main.py add -a 49.99 -d "Groceries from Walmart"
```

### List expenses

```bash
# List all expenses
python main.py list

# Filter by category
python main.py list -c "Food"
```

### Update an expense

```bash
python main.py update -id ID -a AMOUNT -d DESCRIPTION
# Example:
python main.py update -id 1 -a 52.99 -d "Updated description"
```

### Delete an expense

```bash
python main.py delete -id ID
# Example:
python main.py delete -id 1
```

### Get expense summary

```bash
# Get total expenses
python main.py summary

# Get expenses for specific month
python main.py summary -m 5  # For May
```

### Export to CSV

```bash
python main.py to_csv
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

