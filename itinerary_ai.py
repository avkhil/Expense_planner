import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_itinerary(destination, days, budget):
    prompt = f"""
    You are a travel planner. Create a {days}-day travel itinerary for {destination} within a total budget of ₹{budget}.
    Include:
    - Accommodation suggestions
    - Places to visit each day
    - Food options
    - Approximate daily costs
    Return the response as a table with these columns:
    Day | Morning | Afternoon | Evening | Approx Cost (₹)
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # lightweight, cheaper, and fast
        messages=[
            {"role": "system", "content": "You are a helpful AI travel assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


# Example use
if __name__ == "__main__":
    destination = input("Enter destination: ")
    days = int(input("Enter number of days: "))
    budget = int(input("Enter total budget (₹): "))

    itinerary = generate_itinerary(destination, days, budget)
    print("\n✨ Your AI-Generated Itinerary ✨\n")
    print(itinerary)
