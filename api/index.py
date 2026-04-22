from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def webhook():
    return "Bot active"

if __name__ == "__main__":
    app.run()