from flask import Flask, render_template, request
from services.api_client import get_itinerary_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_itinerary', methods=['POST'])
def get_itinerary():
    data = request.form
    from_city = data.get("from_city")
    to_city = data.get("to_city")
    budget = data.get("budget")
    travellers = data.get("travellers")
    days = data.get("days")

    itinerary_html = get_itinerary_data(from_city, to_city, budget, travellers, days)

    return render_template("index.html", result=itinerary_html)

if __name__ == '__main__':
    app.run(debug=True)
