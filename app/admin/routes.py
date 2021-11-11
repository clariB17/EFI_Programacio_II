from flask import app, render_template, redirect, url_for, abort, request, send_file
from flask_login import login_required, current_user
from app.auth.decorators import admin_required
from app.auth.models import User
from app.models import Libro
from . import admin_bp
from .forms import PostForm, UserAdminForm, Libros_upload, Autores_upload

from werkzeug.utils import secure_filename
import os

from app import admin


FOLDER = os.path.abspath('app/static/libros')
EXTENSIONS_LIB = set(['epub', 'pdf'])
EXTENSIONS_IMG = set(['epub', 'pdf'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in EXTENSIONS_LIB

@admin_bp.route("/admin/libro_upload/", methods=['GET', 'POST'])
@login_required
@admin_required
def libro_upload():
    form = Libros_upload()
    if request.method == 'POST':
        if form.validate_on_submit():
            if 'ourfile' not in request.files:
                return 'the form has no file part.'
            f = request.files['ourfile']
            if f.filename == '':
                return 'no file selected'
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(FOLDER, filename))
                return redirect(url_for('admin.get_file', filename=filename))
            return 'file not allowed'
    return render_template('admin/libro_upload.html', form=form)


@admin_bp.route("/admin/autor_upload/", methods=['GET', 'POST'])
@login_required
@admin_required
def autor_upload():
    form = Autores_upload()
    if request.method == 'POST':
        pass
    return render_template('/admin/autor_upload.html', form=form)
    

@admin_bp.route("/admin/uploads/<filename>")
def get_file(filename):
    file = os.path.join(FOLDER, filename)
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