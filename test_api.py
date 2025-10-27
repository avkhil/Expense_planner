import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Make sure .env is in the same folder and contains OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Quick test
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello! This is a test message."}]
)

print(response.choices[0].message.content)
