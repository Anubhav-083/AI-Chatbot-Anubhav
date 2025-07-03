from flask import Flask, render_template, request, jsonify
from chatbot.bot import get_bot_response, log_message

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response_route():
    user_input = request.form["msg"]
    response = get_bot_response(user_input)
    log_message(user_input, response)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
