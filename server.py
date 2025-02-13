from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  

RASA_URL = "http://localhost:5005/webhooks/rest/webhook" 

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return jsonify({"message": "Chatbot is running. Send a POST request with a message."})
    
    if request.content_type != "application/json":
        return jsonify({"error": "Invalid Content-Type. Use application/json"}), 400
    
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    response = requests.post(RASA_URL, json={"sender": "user", "message": user_message})
    
    bot_reply = response.json()
    if bot_reply:
        return jsonify(bot_reply)
    else:
        return jsonify({"response": "I'm sorry, I didn't understand that."})

if __name__ == "__main__":
    app.run(host="192.168.0.109", port=5000, debug=True)
