import json

def read_file(file = "data.json"):
    try:
        with open(file, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
