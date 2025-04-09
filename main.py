from flask import Flask, request
import requests
import json

app = Flask(__name__)

TOKEN = "7860316253:AAG2j8kvMKFmhKKNqWmB3Qq_9ziBS7qLI6Y"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        try:
            data = request.get_json()
            if not data or "message" not in data:
                return "No valid message", 200

            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")

            reply = {
                "chat_id": chat_id,
                "text": f"You said: {text}"
            }

            requests.post(URL, json=reply)
        except Exception as e:
            print("Error:", e)
    return "OK", 200
import os

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
