from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    print("HOME ROUTE CALLED")

    return jsonify({
        "name": "ClippaClipper AI Studio",
        "version": "0.0.1",
        "status": "Online"
    })


@app.route("/ping")
def ping():
    return jsonify({
        "message": "pong"
    })


if __name__ == "__main__":

    print("=" * 50)
    print("ClippaClipper AI Studio")
    print("=" * 50)
    print("Backend Started")
    print("URL : http://127.0.0.1:5000")
    print("=" * 50)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )