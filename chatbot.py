def chatbot_response(user_input):
 
    user_input = user_input.lower() 

    
    if 'hello' in user_input or 'hi' in user_input:
        return "hello how can i  help you today?"
    elif 'how are you' in user_input:
        return "i'm doing well, how about you?"
    elif 'bye' in user_input:
        return "goodbye!"
    elif 'your name' in user_input:
        return "i am a chatbot created by you"
    else:
        return "sorry, i didnt understand that could you try again"

def chat():
    print("Chatbot: hi! type bye  to exit")
    
    while True:
        user_input = input("you: ")

        
        if user_input.lower() == 'bye':
            print("chatbot:goodby!")
            break
        
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    chat()

