from flask import Flask

app = Flask(__name__)

ads = []

@app.route("/")
def index():
    return f"{len(ads)} ads"

@app.route("/ad/<string:slug>/")
def show_post(slug):
    return f"Mostrando el anuncio {slug}"