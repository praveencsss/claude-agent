from google import genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)

system_prompt = """
You are an expert Python coding assistant.
Help with coding, debugging, HTML, CSS, Flask, Python, and projects.
Give clean and beginner-friendly code.
"""

print("🤖 Gemini Coding Assistant Started!")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{system_prompt}\nUser: {user_input}"
        )

        print("\n🤖 AI:\n")
        print(response.text)
        print()

    except Exception as e:
        print("\nError:", e)