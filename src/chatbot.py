from responses import responses
from nlp_utils import preprocess_text

def get_response(user_input):
    tokens = preprocess_text(user_input)
    
    cleaned_input = ' '.join(tokens)

    for key in responses:
        if key in cleaned_input:
            return responses[key]

    return "Sorry, I don't understand that yet."