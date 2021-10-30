from flask import render_template
from . import public_bp
from app.models import Libros
@public_bp.route("/")
def index():
    posts = 'hola'
    return render_template("public/index.html", posts=posts)
