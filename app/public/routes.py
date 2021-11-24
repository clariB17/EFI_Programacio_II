from flask import render_template, send_file, redirect, url_for
from flask_login import login_required, current_user
from . import public_bp
from app.models import Libro, Autor, Deseados
from app import FOLDER_IMAGEN_AUTOR, FOLDER_IMAGEN_LIBRO, FOLDER_LIBRO
import os

@public_bp.route("/")
def index(): 
    libros = Libro.get_last()
    autores = Autor
    likes = []
    if current_user.is_authenticated:
        likes = Deseados.get_by_id_user(current_user.id)
    return render_template("public/index.html", libros=libros, autores=autores, likes=likes)

@public_bp.route('/<id_libro>/<page>')
@login_required 
def like(id_libro, page):
    previus = Deseados.get_liked(current_user.id ,id_libro)
    if previus:
        previus.delete()
        return redirect(url_for('public.%s'%page))
    id_user = current_user.id
    like = Deseados()
    like.id_libro = id_libro
    like.id_user = id_user
    like.save()
    return redirect(url_for('public.%s'%page))

@public_bp.route('/mi_biblioteca')
@login_required 
def mibiblioteca():
    libros = Libro.get_all()
    autores = Autor
    return render_template ('public/mibiblioteca.html', libros=libros, autores=autores)

@public_bp.route('/mis_favoritos')
@login_required 
def misfavoritos():
    deseo = Deseados.get_by_id_user(current_user.id)
    libros = []
    for des in deseo:
        libros.append(Libro.get_by_id(des.id_libro))
    autores = Autor
    likes = []
    if current_user.is_authenticated:
        likes = Deseados.get_by_id_user(current_user.id)
    return render_template ('public/misfavoritos.html', libros=libros, autores=autores, likes=likes)


@public_bp.route("/libros/")
def all_libros():
    libros = Libro.get_all()
    autores = Autor
    likes = []
    if current_user.is_authenticated:
        likes = Deseados.get_by_id_user(current_user.id)
    return render_template("public/libros.html", libros=libros, autores=autores, likes=likes)

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

@public_bp.route("/Contacto")
def contacto():
    return render_template ('public/contacto.html')

@public_bp.route("/acerca")
def acerca():
    return render_template ('public/acerca.html')

