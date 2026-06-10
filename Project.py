# Rule-Based AI Chatbot
responses = {
    "hello": "Hi there!",
    "how are you": "I'm doing great. Thanks for asking!",
    "what is your name": "I'm a Rule-Based AI Chatbot.",
    "thanks": "You're welcome!",
    "bye": "Goodbye! Have a nice day."
}

# Welcome messages
print("Hello! Hope you are having a nice day!")
print("I'm your Rule-Based AI Chatbot.")
print("Tell me what you want, and I'll do my best to help you.")
print("You can type 'exit' anytime to end our conversation.\n")

while True:
    # Get and clean user input
    user_input = input("You: ").lower().strip()

    # Exit condition
    if user_input == "exit":
        print("Bot: Goodbye! Have a wonderful day!")
        break

    # Get response from dictionary
    response = responses.get(
        user_input,
        "Sorry, I don't understand that. Could you please try something else?"
    )
    # Print bot response
    print("Bot:", response)