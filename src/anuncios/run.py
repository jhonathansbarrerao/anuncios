from flask import Flask

app = Flask(__name__)

anuncios = []
@app.route("/")
def index():
    return f"En home hay {len(anuncios)} anuncios"

@app.route("/ad/<string:slug>/")
def show_ad(slug):
    return f"Mostrando el anuncio {slug}"

@app.route("/admin/ad/")
@app.route("/admin/ad/<int:ad_id>/")
def post_form(ad_id=None):
    return f"ad_form {ad_id}"
