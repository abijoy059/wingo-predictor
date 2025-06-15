import requests
from bs4 import BeautifulSoup
import random
from flask import Flask, jsonify

app = Flask(__name__)

# Dummy scrape function (later we will replace with real one)
def scrape_results():
    # এখানে আমরা future এ ওয়েবসাইট থেকে রেজাল্ট আনবো
    # আপাতত ডেমো হিসেবে কিছু ফলাফল দিচ্ছি
    return [random.randint(0, 9) for _ in range(50)]

# Simple ML-like prediction (random choice from top 3 frequent numbers)
def predict_next(results):
    freq = {}
    for r in results:
        freq[r] = freq.get(r, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top_choices = [item[0] for item in sorted_freq[:3]]
    return random.choice(top_choices)

@app.route('/')
def home():
