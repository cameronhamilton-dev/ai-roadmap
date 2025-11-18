import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from gpt_tools import ask_gpt


def summarise_text(text):
    system_message = "You are a summarisation assistant. Summarise the user's text clearly and consisely"
    summary = ask_gpt(prompt=text, system_message=system_message, temperature=0.3)

    return summary


if __name__ == "__main__":
    user_text = input("Please enter the text you would like summarised:\n")
    result = summarise_text(user_text)
    print("\nSummary: \n")
    print(result)
