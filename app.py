from flask import Flask, render_template, request, flash
from services.api_client import get_itinerary_data

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_itinerary', methods=['POST'])
def get_itinerary():
    data = request.form
    from_city = data.get("from_city", "").strip()
    to_city = data.get("to_city", "").strip()
    budget = data.get("budget", "").strip()
    travellers = data.get("travellers", "").strip()
    days = data.get("days", "").strip()

    # Basic Validation
    errors = []
    if not from_city or not to_city:
        errors.append("Please enter both origin and destination cities.")
    if from_city.lower() == to_city.lower():
        errors.append("Origin and destination cannot be the same.")
    try:
        budget = int(budget)
        travellers = int(travellers)
        days = int(days)
        if budget <= 500:
            errors.append("Budget must be at least ₹500 for a valid trip.")
        if travellers <= 0:
            errors.append("Number of travelers must be at least 1.")
        if days <= 0:
            errors.append("Number of days must be at least 1.")
    except ValueError:
        errors.append("Please enter valid numeric values for budget, travelers, and days.")

    # If any validation failed
    if errors:
        for err in errors:
            flash(err)
        return render_template('index.html')

    # If all good, get AI itinerary
    itinerary_html = get_itinerary_data(from_city, to_city, budget, travellers, days)
    return render_template("index.html", result=itinerary_html)

if __name__ == '__main__':
    app.run(debug=True)
s
