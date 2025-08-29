from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm, PostForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'unaclave'

ads = []

@app.route("/")
def index():
    return render_template("index.html", ads=ads)

@app.route("/ad/<string:slug>/")
def show_post(slug):
    return render_template("ad_view.html", slug_title=slug)

@app.route("/admin/ad/", methods=['GET', 'POST'], defaults={'ad_id': None})
@app.route("/admin/ad/<int:ad_id>/", methods=['GET', 'POST'])
def ad_form(ad_id=None):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data
        ad = {'title': title, 'title_slug': title_slug, 'content': content}
        ads.append(ad)
        return redirect(url_for('index'))
    return render_template("admin/ad_form.html", form=form)

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