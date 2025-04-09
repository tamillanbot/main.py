#!/usr/bin/env python3

import cgi
import cgitb
import json
import sys
import urllib.request

# Enable CGI debugging
cgitb.enable()

# Telegram bot token
TOKEN = "7860316253:AAG2j8kvMKFmhKKNqWmB3Qq_9ziBS7qLI6Y"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Read JSON input from Telegram
input_data = sys.stdin.read()
data = json.loads(input_data)

# Extract chat_id and message
chat_id = data["message"]["chat"]["id"]
text = data["message"].get("text", "")

# Build reply
reply = f"Hi! You said: {heloopbro}"

# Send response back to Telegram
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

# Return HTTP response for CGI (must be last)
print("Content-Type: text/html\n")
print("OK")
