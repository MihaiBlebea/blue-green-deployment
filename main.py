from flask import Flask, abort, jsonify
import sys


app = Flask(__name__)
port = sys.argv[1]


@app.route("/healthcheck")
def healthcheck():
    check = {
        "status": "OK2",
        "port": port
    }
    return jsonify(check)

@app.route("/")
def index():
    return "This is the main index route. testing this"

@app.route("/error")
def error_handler():
    abort(500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)