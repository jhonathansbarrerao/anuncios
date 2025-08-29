from flask import Flask

app = Flask(__name__)

ads = []

@app.route("/")
def index():
    return f"{len(ads)} ads"