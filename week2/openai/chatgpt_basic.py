from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("DEBUG: API Key Loaded:", api_key)   # <-- temporary debug line

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Hello from Cameron!"}
    ],
    timeout=10
)

print(response.choices[0].message.content)