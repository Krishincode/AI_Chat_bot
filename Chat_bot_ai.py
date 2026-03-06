# ChatBot_AI_new.py

# Import OpenAI library
from openai import OpenAI

# ================================
# IMPORTANT:
# Replace "YOUR_API_KEY_HERE" with your own OpenAI API key
# Example: sk-proj-xxxxxxxx
# ================================
client = OpenAI(api_key="YOUR_API_KEY_HERE")


def chatbot():
    # Starting message for the user
    print("Hi! OpenAI ChatBot ready hai. Kuch bhi poochho (type 'exit' to quit)")

    # List to store conversation history
    conversation = []

    # Infinite loop so the chatbot keeps running
    while True:
        # Take input from the user
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == "exit":
            print("ChatBot: Bye bro! 🙌")
            break

        # Add user's message to conversation history
        conversation.append({
            "role": "user",
            "content": user_input
        })

        try:
            # Send conversation to OpenAI model
            response = client.chat.completions.create(

                # AI model being used
                model="gpt-4o-mini",

                # Send entire conversation history
                messages=conversation,

                # Controls creativity of response (0 = strict, 1 = creative)
                temperature=0.7,

                # Maximum words/tokens in reply
                max_tokens=200
            )

            # Extract chatbot reply
            answer = response.choices[0].message.content.strip()

            # Print chatbot reply
            print("ChatBot:", answer)

            # Add chatbot reply to conversation history
            conversation.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:
            # If API error occurs
            print("ChatBot: Error hua 😅", e)


# Run chatbot only when this file is executed directly
if __name__ == "__main__":
    chatbot()
