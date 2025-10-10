from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from forms import SignupForm, PostForm, LoginForm
from urllib.parse import urlparse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba2e18ce248bab7ce9425333f0420b57a5f07dfef342e1876d3013a524acf416f813af3071a65e3860475fe8e81c3a42c3c8fa65051de39aa2037fa695b305a7bc7044a415eb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://jhbarrera:class2025@localhost:5432/anuncios'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(app)
login_manager.login_view = 'login'
db = SQLAlchemy(app)
from models import User, Ad

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/")
def index():
    ads = Ad.get_all()
    return render_template("index.html", ads=ads)

@app.route("/ad/<string:slug>/")
def show_post(slug):
    return render_template("ad_view.html", slug_title=slug)

@app.route("/admin/ad/", methods=['GET', 'POST'], defaults={'ad_id': None})
@app.route("/admin/ad/<int:ad_id>/", methods=['GET', 'POST'])
@login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    error = None
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User.get_by_email(email)
        if user is not None:
            error = f'El email {email} ya está registrado'
        else:
            user = User(name=name, email=email)
            user.set_password(password)
            user.save()
            # usuario logueado
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template("admin/signup_form.html", form=form, error=error)


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))