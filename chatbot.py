def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in ['hi', 'hello', 'hey']:
        return "hello, how can I assist you today?"
    if 'return' in user_input or 'exchange' in user_input:
        return "I would be happy to help you with your return or exchange, could you please provide the order number"
    elif 'order number' in user_input:
        return "thank you Can you please tell me the item you'd like to return or exchange"
    elif 'thank you' in user_input:
        return "Your welcome"
    elif 'bye' in user_input:
        return "goodbye"
    else:
        return "sorry, I didn't understand that"

if __name__ == "__main__":
    print("welcome, type bye to end the conversation.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"bot: {response}")
        
        if 'bye' in user_input.lower():
            break
