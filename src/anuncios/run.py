from flask import Flask

app = Flask(__name__)

ads = []

@app.route("/")
def index():
    return f"{len(ads)} ads"

@app.route("/ad/<string:slug>/")
def show_post(slug):
    return f"Mostrando el anuncio {slug}"

@app.route("/admin/ad/")
@app.route("/admin/ad/<int:ad_id>/")
def ad_form(ad_id=None):
    return f"Mostrando el formulario de anuncio {ad_id}"