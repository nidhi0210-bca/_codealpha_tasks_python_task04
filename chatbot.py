def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "your name" in user_input:
        return "I'm ChatPy, your friendly rule-based chatbot!"
    elif "help" in user_input:
        return "Try saying things like 'hello', 'how are you', or 'bye'."
    else:
        return "Hmm... I'm not sure how to respond to that. Try saying 'help'."


def start_chat():
    print("ChatPy is now online! Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print(f"ChatPy: {response}")
        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    start_chat()
