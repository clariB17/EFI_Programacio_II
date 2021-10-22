from flask import abort, render_template, redirect, url_for
from flask_login import current_user

from app.models import Post, Comment
from . import public_bp
from .forms import CommentForm
from app.auth.models import * 

@public_bp.route("/")
def index():
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)

# Un slug es una cadena de caracteres alfanuméricos (más el carácter ‘-‘)
# sin espacios, tildes ni signos de puntuación
@public_bp.route("/p/<string:slug>/", methods=['GET', 'POST'])
def show_post(slug):
    post = Post.get_by_slug(slug)
    if not post:
        abort(404)
    form = CommentForm()
    if current_user.is_authenticated and form.validate_on_submit():
        content = form.content.data
        comment = Comment(content=content, user_id=current_user.id, user_name=current_user.name, post_id=post.id)
        comment.save()
        return redirect(url_for('public.show_post', slug=post.title_slug))
    return render_template("public/post_view.html", post=post, form=form)

@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)