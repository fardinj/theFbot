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
    if not data:
        return "no data"

    message = data.get("message", {})
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    text = message.get("text", "")

    if not chat_id:
        return "no chat id"

    # When user starts the bot
    if text == "/start":
        send_message(chat_id, "👋 Welcome to my bot!")
        send_message(chat_id, f"🆔 Your user ID is: `{chat_id}`")

    return "ok"

if __name__ == "__main__":
    app.run(port=8080)
