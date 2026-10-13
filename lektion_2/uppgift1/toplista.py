from flask import Flask, jsonify, request

app = Flask(__name__)

poangs = [35, 108, 456, 34, 899, 498, 2, 976]

@app.route("/highscores", methods=["GET"])
def get_hogstapoang():
    max_poang = max(poangs)
    return jsonify(max_poang)

@app.route("/highscores", methods=["POST"])
def add_poang():
    data = request.get_json()
    poangs.append(data)
    return jsonify(poangs), 201

#curl.exe -X POST http://127.0.0.1:5000/highscores -H "Content-Type: application/json" -d "(poäng du vill ha)"