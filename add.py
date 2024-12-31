from read_from_json import read_file
from write_to_json import write_to_json
from generate_id import gen_id
from datetime import datetime

def expense_add(amount, description=None):
    content = read_file()
    ID = gen_id(content)
    data = {"ID": ID, 'description': description, 'amount': amount, 'date': datetime.now().replace(second=0, microsecond=0)}
    content.append(data)
    write_to_json(content)
    print(f"# Expense added successfully! (ID: {ID})")
