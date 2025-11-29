# app.py
from flask import Flask, request, jsonify
import os
import openai
import requests

app = Flask(__name__)

# Load API key from environment variable (DO NOT hardcode!)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/solve_quiz", methods=["POST"])
def solve_quiz():
    try:
        data = request.get_json()
        email = data.get("email")
        secret = data.get("secret")
        url = data.get("url")

        if not all([email, secret, url]):
            return jsonify({"error": "Missing one of email, secret, or url"}), 400

        # Example: fetch quiz data from URL (assuming JSON response)
        resp = requests.get(url)
        if resp.status_code != 200:
            return jsonify({"error": "Could not fetch quiz data"}), 400
        quiz_data = resp.json()  # expecting JSON structure

        # Build prompt for OpenAI
        prompt = f"""
        Solve the following quiz for the student {email}.
        Secret info: {secret}
        Quiz Data: {quiz_data}
        Provide answers in JSON format.
        """

        # Call OpenAI GPT API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0
        )

        answer = response["choices"][0]["message"]["content"]

        return jsonify({"email": email, "answers": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
