from flask import Flask, render_template

app = Flask(__name__)

ads = []

@app.route("/")
def index():
    return render_template("index.html", num_ads=len(ads))

@app.route("/ad/<string:slug>/")
def show_post(slug):
    return render_template("ad_view.html", slug_title=slug)

@app.route("/admin/ad/")
@app.route("/admin/ad/<int:ad_id>/")
def ad_form(ad_id=None):
    return render_template("admin/ad_form.html", ad_id=ad_id)

@app.route("/signup/")
def show_signup_form():
    return render_template("admin/signup_form.html")