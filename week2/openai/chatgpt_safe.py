from openai import OpenAI
import requests

from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )

        return response.choices[0].message.content

    except requests.exceptions.Timeout:
        return "Error: The request to OpenAI timed out."

    except Exception as e:
        # This captures ANY OpenAI or network error
        return f"Error calling OpenAI: {e}"


# Test the function
print(ask_gpt("Explain what a Python function is in one sentence."))
