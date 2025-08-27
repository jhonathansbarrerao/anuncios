from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

anuncios = []
@app.route("/")
def index():
    return render_template("index.html", num_ads=len(anuncios))

@app.route("/ad/<string:slug>/")
def show_ad(slug):
    return render_template("ad_view.html", slug_title=slug)

@app.route("/admin/ad/")
@app.route("/admin/ad/<int:ad_id>/")
def ad_form(ad_id=None):
    return render_template("admin/ad_form.html", ad_id=ad_id)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html")

