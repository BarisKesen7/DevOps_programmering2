from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Hej världen"


@app.route("/api/hej/<namn>")
def hej(namn):
    return jsonify({"hälsning": f"Hej {namn}"})
