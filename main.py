
from flask import Flask, request
import json
import urllib.request

app = Flask(__name__)

TOKEN = "7860316253:AAG2j8kvMKFmhKKNqWmB3Qq_9ziBS7qLI6Y"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Received data:", data)  # Optional: For debugging

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        reply = f"Hi! You said: {text}"

        params = {
            "chat_id": chat_id,
            "text": reply
        }

        req = urllib.request.Request(
            API_URL,
            data=json.dumps(params).encode(),
            headers={"Content-Type": "application/json"}
        )
        urllib.request.urlopen(req)

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
