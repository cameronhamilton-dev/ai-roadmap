from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'system', 'content': 'You are a friendly assistant.'},
        {'role': 'user', 'content': 'Explain what an api is in one sentence'}
    ],
    temperature=0.7,
    max_tokens=100
)

print(response.choices[0].message.content)

#   ✔ system message: This defines the assistant’s role / behavior. Think of it as personality + rules.

#   ✔ temperature=0.7: Controls randomness: 0.0 = deterministic 1.0 = creative

#   ✔ max_tokens=100: Controls output length (safety + cost awareness).