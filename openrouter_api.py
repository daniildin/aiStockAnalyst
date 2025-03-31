import requests

API_KEY = "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"

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "openai/gpt-4o",  # Optional, specify model if needed
        "messages": [
            {"role": "user", "content": "What is the meaning of life?"}
        ]
    }
)

print(response.json())  # Print the API response
