from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)


@app.route("/api/tid")
def hamta_tid():
    lokal_tid = datetime.now()
    utc_tid = datetime.now(timezone.utc)

    return jsonify(
        {
            "timezon": "Europa/Stockholm",
            "local time": lokal_tid.strftime("%Y-%m-%d %H:%M:%S"),
            "utc time": utc_tid.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
