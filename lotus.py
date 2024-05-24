from openai import OpenAI
import json

client = OpenAI(api_key="sk-proj-3hMVPnHfrP1OaSEiqa7vT3BlbkFJoCNV4TOwiVqhV0PI2QGo")

data = [] # Insert your product list here

system_message = {
                    "role": "system",
                    "content": "You are a helpful personal assistant named Lotus."
                  }

conversation = [system_message]

count = 0

# Loop to interactively ask questions from the terminal
while True:
    
    if (count == 0):
        print("Assistant: Hi, how may I help you?")

    user_input = input("You: ") # Get user input for the next question]

    
    user_message = {"role": "user", "content": user_input} # Add user message to the conversation
    conversation.append(user_message)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=conversation)

    assistant_reply = response.choices[0].message.content
    print(f"Assistant: {assistant_reply}")
    print("-" * 50)

    conversation.append({"role": "assistant", "content": assistant_reply}) # Include the assistant's response in the conversation for context in the next turn

    count += 1