from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form.get("Body", "").strip()
    resp = MessagingResponse()
    msg = resp.message()

    msg.body(f"Hola 👋 Recibí tu mensaje: '{incoming_msg}'. ¡El bot está funcionando!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    