from datetime import datetime
from tabulate import tabulate
import json


def read_file(file="data.json"):
    try:
        with open(file, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def write_to_json(data, file="data.json"):
    with open(file, "w") as file:
        json.dump(data, file)


def expense_add(amount, description=None):
    if amount or description:
        content = read_file()
        ID = gen_id(content)
        data = {"ID": ID, 'description': description, 'amount': amount,
                'created_at': str(datetime.now().replace(second=0, microsecond=0)),
                'updated_at': str(datetime.now().replace(second=0, microsecond=0)),
                }
        content.append(data)
        write_to_json(content)
        print(f"# Expense added successfully! (ID: {ID})")
    else:
        print("Provide amount or description data")


def gen_id(data):
    if not data:
        return 1
    else:
        return max(item['ID'] for item in data) + 1


def expense_list():
    content = read_file()
    if not content:
        return
    else:
        print(tabulate(content, headers="keys", tablefmt="grid"))


def expense_update_by_id(ID: int, amount: float = None, description: str = None):
    file_content = read_file()

    if amount or description:
        id_found = False
        ID = int(ID)
        for item in file_content:
            if item['ID'] == ID:
                id_found = True
                if amount:
                    item['amount'] = amount
                    item['updated_at'] = str(datetime.now().replace(second=0, microsecond=0))
                if description:
                    item['description'] = description
                    item['updated_at'] = str(datetime.now().replace(second=0, microsecond=0))
                write_to_json(file_content)
                print(f"Item ID {ID} changed successfully")
        if not id_found:
            print(f"Item with ID {ID} not found")
    else:
        print("No amount or description data provided")


def expense_delete(ID: int):
    file_content = read_file()
    if file_content:
        ID = int(ID)
        original_length = len(file_content)
        data = [item for item in file_content if item['ID'] != ID]
        new_length = len(data)
        if new_length < original_length:
            write_to_json(data)
            print(f"Successfully deleted item with ID {ID}")
        else:
            print(f"No changes occurred. Maybe there is no item with such ID?")
    else:
        print(f"No data to delete")


def expense_summary(month: int = 0):
    content = read_file()
    count = 0
    if month:
        for item in content:
            expense_date = datetime.strptime(item['created_at'], '%Y-%m-%d %H:%M:%S')
            if expense_date.month == month:
                count += item['amount']
        print(f"Expenses in month {month}: {count}")

    else:
        for item in content:
            count += item['amount']
        print(f"Expenses overall: {count}")
