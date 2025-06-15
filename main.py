import requests
from bs4 import BeautifulSoup
import random
from flask import Flask, jsonify

app = Flask(__name__)

# Dummy scrape function
def scrape_results():
    # ভবিষ্যতে এখানে ওয়েবসাইট থেকে আসল রেজাল্ট আনবে
    return [random.randint(0, 9) for _ in range(50)]

# Prediction function (most frequent 3 থেকে random)
def predict_next(results):
    freq = {}
    for r in results:
        freq[r] = freq.get(r, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top_choices = [item[0] for item in sorted_freq[:3]]
    return random.choice(top_choices)

# Home route (test if working)
@app.route('/')
def home():
    return "Wingo Prediction API is running!"

# Prediction API route
@app.route('/predict')
def predict():
    results = scrape_results()
    next_prediction = predict_next(results)
    return jsonify({
        "past_results": results,
        "next_prediction": next_prediction
    })

# Entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
