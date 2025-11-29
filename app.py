from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Your secret from Google Form
MY_SECRET = "My name is Jainish Shah. I am doing a dual degree. I am doing Diploma in Data Science and Programming from IIT Madras. Additionally I am doing B.Tech in Electronics and Communication Engineering from Institute of Technology, Nirma University. Hey! This is the secret key for my Tools in Data Science Project 2."

@app.route("/solve_quiz", methods=["POST"])
def solve_quiz():
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    email = data.get("email")
    secret = data.get("secret")
    url = data.get("url")

    # Check secret
    if secret != MY_SECRET:
        return jsonify({"error": "Invalid secret"}), 403

    # Here you would write your code to fetch the quiz page, solve it, and submit
    # For demo, we just return a fixed response
    return jsonify({"status": "success", "message": "Quiz solved placeholder", "url": url}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
