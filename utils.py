import json
def load_data():
    with open('static/data/notes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data