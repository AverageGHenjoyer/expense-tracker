from actions import *
import argparse

parser = argparse.ArgumentParser(prog="expense-tracker", description="Add, list oe summarize your expenses!")
parser.add_argument('action', help="Action to take. Can be: add, list, summary, delete", type=str)
parser.add_argument("-id", type=str)
parser.add_argument('-a', '--amount', type=float, default=0)
parser.add_argument('-d', '--description', type=str)

args = parser.parse_args()

match args.action:
    case "add":
        expense_add(amount=args.amount, description=args.description)

    case "list":
        expense_list()

    case "ls":
        expense_list()

    case "update":
        expense_update_by_id(ID=args.id, amount=args.amount, description=args.description)

    case "delete":
        expense_delete(ID=args.id)
