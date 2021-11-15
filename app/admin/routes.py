from flask import render_template, redirect, url_for, abort, request, send_file
from flask_login import login_required, current_user
from app.auth.decorators import admin_required
from app.auth.models import User
from app.models import Genero, Libro, Genero, Pais, Autor, Idioma
from . import admin_bp
from .forms import PostForm, UserAdminForm, Libros_upload, Autores_upload
from werkzeug.utils import secure_filename
import os



FOLDER_LIBRO = os.path.abspath('app/static/libros')
FOLDER_IMAGEN_LIBRO = os.path.abspath('app/static/img_libro')
FOLDER_IMAGEN_AUTOR = os.path.abspath('app/static/img_autor')
EXTENSIONS_LIB = set(['epub', 'pdf'])
EXTENSIONS_IMG = set(['png', 'jpeg', 'jpg'])


def libro_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in EXTENSIONS_LIB

def imagen_permitida(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in EXTENSIONS_IMG

@admin_bp.route("/admin/libro_upload/", methods=['GET', 'POST'])
@login_required
@admin_required
def libro_upload():
    form = Libros_upload()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.titulo.data
            isbn = form.ISBN.data
            precio = form.precio.data
            genero = form.genero.data
            autor = form.autor.data
            idioma = form.idioma.data

            codigo = Libro.get_by_name(isbn)
            if codigo is not None:
                error = 'ERROR: El ISBN %s ya está siendo utilizado por otro usuario' %isbn
                return render_template('admin/libro_upload.html', form=form, error=error)
            
            if genero == None or idioma == None or autor == None:
                error = 'ERROR: Campo de seleccion incompleto'
                return render_template('admin/libro_upload.html', form=form, error=error)
            
            if ('libro' not in request.files) and ('imagen' not in request.files):
                error = 'ERROR: No se encontro el archivo esperado.'
                return render_template('admin/libro_upload.html', form=form, error=error)

            f = request.files['libro']
            i = request.files['imagen']

            if f.filename == '' and i.filename == '':
                error = 'ERROR: Nombre de archivo en blanco'
                return render_template('admin/libro_upload.html', form=form, error=error)

            if (f and libro_permitido(f.filename)) and (i and imagen_permitida(i.filename)):
                libro_name = secure_filename(f.filename)
                f.save(os.path.join(FOLDER_LIBRO, libro_name))

                imagen_name = secure_filename(i.filename)
                i.save(os.path.join(FOLDER_IMAGEN_LIBRO, imagen_name))

                libro = Libro()
                libro.titulo = name
                libro.ISBN = isbn
                libro.precio = precio
                libro.id_genero = Genero.get_by_name(genero.nombre).id
                libro.id_autor =  Autor.get_by_name(autor.nombre).id
                libro.id_idioma = Idioma.get_by_name(idioma.nombre).id
                libro.ruta_foto = imagen_name 
                libro.ruta_libro = libro_name
                libro.save()

                return redirect(url_for('admin.get_libro', filename=libro_name))
            error = 'ERROR: Extencion de archivo no permitida'
            return render_template('admin/libro_upload.html', form=form, error=error)
    return render_template('admin/libro_upload.html', form=form)


@admin_bp.route("/admin/autor_upload/", methods=['GET', 'POST'])
@login_required
@admin_required
def autor_upload():
    form = Autores_upload()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.nombre.data
            apellido = form.apellido.data
            fecha_de_nacimiento = form.fecha_de_nacimiento.data
            pais = form.pais.data

            print('entre12312')
            if pais == None:
                error = 'ERROR: Campo de seleccion incompleto'
                return render_template('admin/autor_upload.html', form=form, error=error)
            
            if 'imagen' not in request.files:
                error = 'ERROR: No se encontro el archivo esperado.'
                return render_template('admin/autor_upload.html', form=form, error=error)

            i = request.files['imagen']

            if i.filename == '':
                error = 'ERROR: Nombre de archivo en blanco'
                return render_template('admin/autor_upload.html', form=form, error=error)

            if i and imagen_permitida(i.filename):
                print('entre')
                imagen_name = secure_filename(i.filename)
                i.save(os.path.join(FOLDER_IMAGEN_AUTOR, imagen_name))

                autor = Autor()
                autor.nombre = name
                autor.apellido = apellido
                autor.fecha_de_nacimiento = fecha_de_nacimiento
                autor.ruta_foto = imagen_name
                autor.id_pais = Pais.get_by_name(pais.nombre).id
                autor.save()

                return redirect(url_for('admin.get_autor', filename=imagen_name))
            error = 'ERROR: Extencion de archivo no permitida'
            return render_template('admin/autor_upload.html', form=form, error=error)
        error = 'formulario invalido'
        return render_template('admin/autor_upload.html', form=form, error=error)
    return render_template('/admin/autor_upload.html', form=form)
    
# para pruebas
@admin_bp.route("/admin/uploads/<filename>")
def get_autor(filename):
    file = os.path.join(FOLDER_IMAGEN_AUTOR, filename)
    return send_file(file)

@admin_bp.route("/admin/uploads/<filename>")
def get_libro(filename):
    file = os.path.join(FOLDER_LIBRO, filename)
    return send_file(file)






@admin_bp.route("/admin/")
@login_required
@admin_required
def index():
    return render_template("admin/index.html")

@admin_bp.route("/admin/posts/")
@login_required
@admin_required
def list_posts():
    posts = Libro.get_all()
    return render_template("admin/posts.html", posts=posts)

@admin_bp.route("/admin/post/", methods=['GET', 'POST'])
@login_required
@admin_required
def post_form():
    #   Crea un nuevo post   #
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        post = Libro(user_id=current_user.id, title=title, content=content)
        post.save()
        return redirect(url_for('admin.list_posts'))
    return render_template("admin/post_form.html", form=form)

@admin_bp.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_post_form(post_id):
    #   Actualiza un post existente   #
    post = Libro.get_by_id(post_id)
    if post is None:
        abort(404)
    # Crea un formulario inicializando los campos con
    # los valores del post.
    form = PostForm(obj=post)
    if form.validate_on_submit():
        # Actualiza los campos del post existente
        post.title = form.title.data
        post.content = form.content.data
        post.save()
        return redirect(url_for('admin.list_posts'))
    return render_template("admin/post_form.html", form=form, post=post)

@admin_bp.route("/admin/post/delete/<int:post_id>/", methods=['POST', ])
@login_required
@admin_required
def delete_post(post_id):
    post = Libro.get_by_id(post_id)
    if post is None:
        abort(404)
    post.delete()
    return redirect(url_for('admin.list_posts'))

@admin_bp.route("/admin/user/<int:user_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_user_form(user_id):
    # Acá entra para actualizar un usuario existente
    user = User.get_by_id(user_id)
    if user is None:
        abort(404)
    # Crea un formulario inicializando los campos con los valores del usuario.
    form = UserAdminForm(obj=user)
    if form.validate_on_submit():
        # Actualiza los campos del usuario existente
        user.is_admin = form.is_admin.data
        user.save()
        return redirect(url_for('admin.list_users'))
    return render_template("admin/user_form.html", form=form, user=user)

@admin_bp.route("/admin/user/delete/<int:user_id>/", methods=['POST', ])
@login_required
@admin_required
def delete_user(user_id):
    user = User.get_by_id(user_id)
    if user is None:
        abort(404)
    user.delete()
    return redirect(url_for('admin.list_users'))

@admin_bp.route("/admin/users/")
@login_required
@admin_required
def list_users():
    users = User.get_all()
    return render_template("admin/users.html", users=users)