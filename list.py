from read_from_json import read_file
from tabulate import tabulate

def expense_list():
    content = read_file()
    if not content:
        return
    else:
        print(tabulate(content, headers="keys", tablefmt="grid"))
