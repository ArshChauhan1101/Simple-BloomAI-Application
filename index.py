import requests

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = {"Authorization": "Bearer API"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")
    return response.json()

def chatbot():
    print("Welcome to the AI chatbot! Type 'exit' to end the conversation.")
    conversation_history = ""

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        conversation_history += f"You: {user_input}\n"

        payload = {
            "inputs": conversation_history
        }

        try:
            response = query(payload)
            chatbot_response = response[0]["generated_text"]
        except Exception as e:
            print(f"Error: {e}")
            continue

        conversation_history += f"Chatbot: {chatbot_response}\n"
        print(f"Chatbot: {chatbot_response}")

# Run the chatbot
chatbot()
