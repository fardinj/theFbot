from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "594895980:-cUyxtkPLAKGpdsLOvrMK4rbLTi1_W3Udms"
BASE_URL = f"https://tapi.bale.ai/bot{TOKEN}"

def send_message(chat_id, text):
    requests.post(f"{BASE_URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

@app.route("/", methods=["POST"])
def handle_update():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Handle /start command
        if text == "/start":
            send_message(chat_id, "👋 Hey there! Welcome to my bot.")
            send_message(chat_id, "Here’s what I can do for you...")
            send_message(chat_id, "Type /help to get started.")

    return "ok"

if __name__ == "__main__":
    app.run(port=8080)

