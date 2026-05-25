import requests

# Store conversation history
chat_history = []

# Function to send message to Ollama
def chat_with_gemma(user_message):

    global chat_history

    # Add user message
    chat_history.append({
        "role": "user",
        "content": user_message
    })

    # Keep last 5 messages
    chat_history = chat_history[-5:]

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "gemma3:1b",
                "messages": chat_history,
                "stream": False
            }
        )

        # Convert response to JSON
        data = response.json()

        # Extract assistant reply
        bot_reply = data["message"]["content"]

        # Save assistant response
        chat_history.append({
            "role": "assistant",
            "content": bot_reply
        })

        return bot_reply

    except Exception as error:
        return f"Error: {error}"


# Main loop
def main():

    print("=== Gemma AI Chatbot ===")
    print("Type 'exit' to quit.\n")

    while True:

        user_text = input("You: ")

        if user_text.lower() == "exit":
            print("Chat ended.")
            break

        reply = chat_with_gemma(user_text)

        print("\nGemma:", reply)
        print()


# Run program
main()