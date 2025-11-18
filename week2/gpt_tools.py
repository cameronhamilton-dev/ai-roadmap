from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_gpt(
    prompt: str,
    system_message: str = "You are a helpful AI assistant.",
    temperature: float = 0.7,
    max_tokens: int = 200,
):
    """
    A reusable function to call the ChatGPT API safely.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=15,
        )

        return response.choices[0].message.content

    except requests.exceptions.Timeout:
        return "Error: The request timed out."

    except Exception as e:
        return f"Error calling OpenAI: {e}"
