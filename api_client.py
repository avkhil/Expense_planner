from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in environment variables. Check your .env file.")

# Initialize OpenAI client properly
client = OpenAI(api_key=api_key)

def get_itinerary_data(from_city, to_city, budget, travellers, days):
    prompt = f"""
    Generate a travel itinerary for {travellers} travelers from {from_city} to {to_city} 
    for {days} days within a total budget of ₹{budget}.
    Include daily activities, hotel suggestions, transport, and food cost breakdown.
    Display results in a clean HTML table.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
