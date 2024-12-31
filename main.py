import argparse
from add import expense_add
from list import expense_list

parser = argparse.ArgumentParser(prog="expense-tracker", description="Add, list oe summarize your expenses!")
parser.add_argument('action', help="Action to take. Can be: add, list, summary, delete", type=str)
parser.add_argument('-a', '--amount', type=float, default=0)
parser.add_argument('-d', '--description', type=str)
args = parser.parse_args()

match args.action:
    case "add":
        expense_add(amount=args.amount, description=args.description)

    case "list":
        expense_list()



