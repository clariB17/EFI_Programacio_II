from flask import render_template
from . import public_bp
from app.models import Libro

@public_bp.route("/")
def index():
    return render_template("public/index.html", )
