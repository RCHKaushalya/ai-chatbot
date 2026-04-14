from chatbot import get_response

print("Simple AI Chatbot Started")
print("Type 'quit' to exit")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'quit':
        print("Bot: Goodbye!")
        break
    
    response = get_response(user_input)
    print(f"Bot: {response}")