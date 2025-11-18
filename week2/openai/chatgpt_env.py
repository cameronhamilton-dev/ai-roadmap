from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read environment variable
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Say hello! You are running from a safe environment variable."}
    ]
)

print(response.choices[0].message.content)
