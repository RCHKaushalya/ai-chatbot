import random
from nlp_utils import preprocess_text
from data_loader import load_intents

intents = load_intents()

def get_response(user_input):
    tokens = preprocess_text(user_input)
    cleaned_input = ' '.join(tokens)

    for intent in intents:
        for pattern in intent['patterns']:
            if pattern in cleaned_input:
                return random.choice(intent['responses'])

    return "Sorry, I don't understand that yet."