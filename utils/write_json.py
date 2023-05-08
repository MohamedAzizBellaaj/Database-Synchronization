import json


def write_json(new_data, filename):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=2)
