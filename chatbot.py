import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a financial assistant."},
                  {"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(chat_with_ai("Tell me about Tesla stock."))
