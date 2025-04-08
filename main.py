from flask import Flask, request
import json
import urllib.request

app = Flask(__name__)

TOKEN = "7860316253:AAG2j8kvMKFmhKKNqWmB3Qq_9ziBS7qLI6Y"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "message" in data:
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
        from flask import Flask, request
import json
import urllib.request

app = Flask(__name__)

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# ✅ Handle GET request to root for browser / Render health checks
@app.route("/", methods=["GET"])
def index():
    return "Bot is running!"

# ✅ Telegram webhook will POST data here
@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "message" in data:
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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
