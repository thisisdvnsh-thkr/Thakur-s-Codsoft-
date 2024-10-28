def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How are you? How can I help you?"
    
    elif "how are you" in user_input:
        return "I'm good and I'm here to help you! How can I assist you?"
    
    elif "do i know you?" in user_input:
        return "Yes, I'm here to help you! You can call me ChatBot!"
    
    elif "goodbye" in user_input or "bye" in user_input:
        return "Goodbye! Will meet again! Have a great day!"
    
    elif "thank you" in user_input:
        return "You're welcome! If you need more help, feel free to ask!"
    
    else:
        return "I don't know about it. Can you please rephrase or ask something else?"
    
# Example usage
while True:
    user_input = input("Me: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("ChatBot:",response)
