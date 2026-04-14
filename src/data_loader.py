import json

def load_intents():
    with open('data/intents.json', 'r') as file:
        data = json.load(file)
    
    return data['intents']