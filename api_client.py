import os
from openai import OpenAI
from dotenv import load_dotenv
import markdown

load_dotenv()

def get_itinerary_data(from_city, to_city, days, travellers, budget):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
    Plan a {days}-day travel itinerary from {from_city} to {to_city} for {travellers} travellers
    within a total budget of ₹{budget}.
    Include hotel options, food costs, travel (both ways + local), and daily activities.
    Break down day-wise expenses and show how much each person will spend.
    Present the output as a Markdown table with these columns:
    | Day | Activity | Hotel | Food | Transport | Total (₹) | Per Person (₹) |
    At the end, summarize total cost and remaining budget (if any).
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    text_response = response.choices[0].message.content

    # Convert Markdown (like | tables |) into HTML tables
    html_response = markdown.markdown(text_response, extensions=["tables"])

    return html_response
