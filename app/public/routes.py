from flask import render_template
from . import public_bp

@public_bp.route("/")
def index():
    posts = 'hola'
    return render_template("public/index.html", posts=posts)
