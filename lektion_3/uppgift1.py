from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route("/app")
def main():

    highscores = {
        "ID": ["Yunus", "Samet", "Elif", "Baris"],
        "Score": ["5", "234", "578", "987"]
    }
    df = pd.DataFrame(highscores)

    tabell_html = df.to_html(classes="table table-striped table-hover", index=False, justify="left")
    stapeldiagram = px.bar(df, x="ID", y="Score", title="HIGHSCORES")
    diagram_html = stapeldiagram.to_html(full_html=False)

    return render_template("index.html", tabell = tabell_html, diagram = diagram_html)

if __name__ == "__main__":
    app.run(debug=True)

