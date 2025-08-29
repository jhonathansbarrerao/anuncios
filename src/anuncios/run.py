from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'unaclave'

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

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("admin/signup_form.html", form=form)