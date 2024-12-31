import json


def write_to_json(data, file="data.json"):
    with open(file, "w") as file:
        json.dump(data, file)
