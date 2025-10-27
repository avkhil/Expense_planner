from modules.ai_itinerary import generate_itinerary

result = generate_itinerary("Delhi", 4, 5000)

if result:
    print(result)
else:
    print("Itinerary generation failed or API not active.")
