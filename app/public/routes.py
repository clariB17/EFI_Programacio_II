from flask import render_template
from . import public_bp
from app.models import Libro, Autor


@public_bp.route("/")
def index():
    libros = Libro.get_last()
    autores = Autor
    return render_template("public/index.html", libros=libros, autores=autores)

@public_bp.route("/libros/")
def all_libros():
    libros = Libro.get_all()
    autores = Autor
    return render_template("public/libros.html", libros=libros, autores=autores)

#tenemos que charlar la compra
@public_bp.route("/comprar/<id_libro>")
def buy_libro():
    pass