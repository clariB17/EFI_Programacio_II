from flask import render_template, send_file, request, redirect, url_for
from flask_login import login_required, current_user
from . import public_bp
from app.models import Libro, Autor, Deseados
from app import FOLDER_IMAGEN_AUTOR, FOLDER_IMAGEN_LIBRO, FOLDER_LIBRO
import os
from app.auth.models import User


@public_bp.route("/")
def index(): 
    libros = Libro.get_last()
    autores = Autor
    like = Deseados
    return render_template("public/index.html", libros=libros, autores=autores)

@login_required
@public_bp.route('/<id_libro>', methods=['GET', 'POST'])
def like(id_libro):
    if Deseados.get_liked(current_user.id ,id_libro):
        return render_template('public/test.html', test=Deseados.get_liked(current_user.id, id_libro))
        # id_user = current_user.id
        # like = Deseados()
        # like.id_libro = id_libro
        # like.id_user = id_user
        # like.save()
    return render_template('public/test.html', test='nada')


@public_bp.route("/libros/")
def all_libros():
    libros = Libro.get_all()
    autores = Autor
    return render_template("public/libros.html", libros=libros, autores=autores)

# para leer libros
@public_bp.route("/leer/<id_libro>")
def read_libro(id_libro):
    filename = Libro.get_by_id(id_libro).ruta_libro
    rute = os.path.join(FOLDER_LIBRO, filename)
    return send_file(rute)

# descargar libro
@public_bp.route("/download/<id_libro>")
def download_libro(id_libro):
    filename = Libro.get_by_id(id_libro).ruta_libro
    rute = os.path.join(FOLDER_LIBRO, filename)
    return send_file(rute, as_attachment=True)