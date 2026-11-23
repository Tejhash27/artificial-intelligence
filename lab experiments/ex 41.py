# Simple Chatbot using NLP Techniques

import re
import random

# Chatbot responses
responses = {
    "hello": [
        "Hello! How are you?",
        "Hi! Nice to meet you."
    ],
    "how are you": [
        "I am fine. Thank you!",
        "I am doing great!"
    ],
    "your name": [
        "My name is ChatBot.",
        "I am a simple Python chatbot."
    ],
    "what is python": [
        "Python is a popular programming language."
    ],
    "thank you": [
        "You are welcome!",
        "Happy to help!"
    ],
    "bye": [
        "Goodbye! Have a nice day!"
    ]
}

print("================================")
print("       SIMPLE NLP CHATBOT       ")
print("================================")
print("ChatBot: Hello! Welcome to my chatbot.")
print("ChatBot: Type 'bye' to exit.")

while True:

    user_input = input("\nYou: ").lower()

    # Remove special characters
    cleaned_input = re.sub(r'[^a-z0-9 ]', '', user_input)

    # Tokenization
    words = cleaned_input.split()

    found = False

    # Match user input with known patterns
    for key in responses:

        key_words = key.split()

        if all(word in words for word in key_words):
            print("ChatBot:", random.choice(responses[key]))
            found = True
            break

    # Default response
    if not found:
        print("ChatBot: Sorry, I don't understand. Please try another question.")

    # Exit chatbot
    if "bye" in words:
        break

print("\nChatbot session ended successfully!")
