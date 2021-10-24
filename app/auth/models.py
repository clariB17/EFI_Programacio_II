from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

# AHORA LA CLASE USER HEREDA LA CLASE MODEL DE SQLALCHEMY
class User(db.Model, UserMixin):

    __tablename__ = 'Users'
    # DEFINIMOS LA CLAVE PRIMARIA
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, name, username):
        self.name = name
        self.username = username

    def __repr__(self):
        return 'User %s>' %self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    # CAMBIAMOS get_user(username) POR EL METODO get_by_username(username) DE LA CLASE USER
    def get_by_username(username):
        return User.query.filter_by(username=username).first()
