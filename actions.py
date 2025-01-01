from generate_id import gen_id
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
    content = read_file()
    ID = gen_id(content)
    data = {"ID": ID, 'description': description, 'amount': amount,
            'created_at': str(datetime.now().replace(second=0, microsecond=0))
            }
    content.append(data)
    write_to_json(content)
    print(f"# Expense added successfully! (ID: {ID})")


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
    for item in file_content:
        if (amount or description) and item['ID'] == ID:
            if amount:
                item['amount'] = amount
                item['updated_at'] = datetime.now().replace(second=0, microsecond=0)
            if description:
                item['description'] = description
                item['updated_at'] = str(datetime.now().replace(second=0, microsecond=0))
            print(f"Item ID {ID} changed successfully")
