from actions import *
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="action", required=True, help="Subcommands")

add_parser = subparsers.add_parser("add", help="Add new expense")
add_parser.add_argument("-a", "--amount", type=float, required=True)
add_parser.add_argument("-d", "--description", type=str, required=True)

list_parser = subparsers.add_parser("list", help="List all expenses")
# list_parser.add_argument("-")
update_parser = subparsers.add_parser("update", help="Update an expense")
update_parser.add_argument("-id", type=int)
update_parser.add_argument("-a", "--amount", type=float)
update_parser.add_argument("-d", "--description", type=str)

delete_parser = subparsers.add_parser("delete", help="Delete an expense")
delete_parser.add_argument("-id", type=int)

summary_parser = subparsers.add_parser("summary", help="Summarize an expense")
summary_parser.add_argument("-m", "--month", choices=range(1, 13), type=int, help="Month number (1-12)")

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

    case "summary":
        expense_summary(month=args.month)
