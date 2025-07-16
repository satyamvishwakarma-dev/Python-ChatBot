import pyjokes

print("Hello! I'm ByteBot.\nType 'bye' to exit.")

while True:
    joke = pyjokes.get_joke()
    user_input = input("You: ").lower()
    if user_input == "bye" or 'exit' in user_input:
        print("ByteBot: Bye!!\nCatch you later.")
        break

    elif 'hello' in user_input or 'hi' in user_input:
        print("ByteBot: Hi There!!\nnice to meet you")

    elif 'how are you' in user_input:
        print("ByteBot: I'm fine, How about You?")

    elif 'i am also fine' in user_input:
        print("ByteBot: That's great, What can i help you with?")

    elif 'your name' in user_input or 'who are you?' in user_input:
        print("ByteBot: My name is ByteBot, you chat companion")

    elif 'what can you do' in user_input:
        print("ByteBot: I can chat with you and make your coding journey less lonely!")

    elif 'who created you' in user_input:
        print("ByteBot: I was created by Satyam — a smart coder in the making!")

    elif 'are you real' in user_input:
        print("ByteBot: I'm as real as your imagination 😉.")

    elif 'what is your age' in user_input:
        print("ByteBot: I was born the moment you ran this code!")

    elif 'thank you' in user_input:
        print("ByteBot: Anytime, friend!")

    elif 'tell me a joke' in user_input or 'joke' in user_input:
        print(f"ByteBot: {joke} 😂")

    elif 'are you smart' in user_input or 'you are smart' in user_input:
        print("ByteBot: I’m learning from the best — you!")

    elif 'do you sleep' in user_input:
        print("ByteBot: Nope. I'm a bot — I run on logic, not dreams.")

    elif 'how to learn coding' in user_input:
        print("ByteBot: Practice every day. Start small, stay consistent. You're already on the right path!")

    elif 'what is dsa' in user_input:
        print("ByteBot: DSA means Data Structures and Algorithms — the building blocks of smart coding.")

    else:
        print("ByteBot: Hmm... I didn’t get that. Try asking something else.\nI am still under development")