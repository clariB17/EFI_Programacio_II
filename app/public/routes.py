from flask import render_template
from . import public_bp
from app.models import Libro

@public_bp.route("/")
def index():
    libros = Libro.get_all()
    return render_template("public/index.html", libros = libros)
