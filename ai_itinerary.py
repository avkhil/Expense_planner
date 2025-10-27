# modules/ai_itinerary.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_itinerary(destination, days, budget):
    """
    Generates a travel itinerary using OpenAI API.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️ API key not found. Please check your .env file.")
        return None

    try:
        client = OpenAI(api_key=api_key)
        prompt = f"""
        Create a {days}-day travel itinerary for {destination} under a total budget of ₹{budget}.
        Include daily breakdown of activities, estimated costs, and short descriptions.
        Present the data in a clear table with columns: Day, Activity, Estimated Cost (₹), and Notes.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ API error: {e}")
        return None
