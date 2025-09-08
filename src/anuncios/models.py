from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):

    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return '<User {}>'.format(self.email)