from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/myapi")
def sida_med_api():
    url = "https://lichess.org/api/player/top/10/blitz"

    data = requests.get(url)
    api_data = data.json()

    topplista = api_data["users"]

    return render_template("api.html", spelare=topplista)

if __name__ == "__main__":
    app.run(debug=True)