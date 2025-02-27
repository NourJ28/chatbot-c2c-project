def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if 'return' in user_input or 'exchange' in user_input:
        return "I would be happy to help you with your return or exchange. Could you please provide the order number"
    elif 'order number' in user_input:
        return "thank you can you please tell me the item you'd like to return or exchange."
    elif 'thank you' in user_input:
        return "youre welcome"
    elif 'bye' in user_input:
        return "Goodbye"
    else:
        return "Sorry, I didn't understand that?"

if __name__ == "__main__":
    print(chatbot_response("exchange"))
