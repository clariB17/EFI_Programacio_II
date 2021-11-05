from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate 
# IMPORTAMOS SQLALCHEMY 
from flask_sqlalchemy import SQLAlchemy
# IMPORTAMOS EL MANEJADOR DE MYSQL
from pymysql import *

login_manager = LoginManager()
# CREAMOS EL OBJETO SQLALCHEMY
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    # LE DECIMOS A LA APP DONDE SE ENCUENTRA LA BASE DE DATOS
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://BD2021:BD2021itec@143.198.156.171/editorial'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
<<<<<<< HEAD

    # Configuración del email
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = ''
    app.config['MAIL_PASSWORD'] = ''
    app.config['DONT_REPLY_FROM_EMAIL'] = ''
    app.config['ADMINS'] = ('', )
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_DEBUG'] = False

=======
    
>>>>>>> e8b49cad981d84b86ca0bba7fbd3e6a0e52ac542
    login_manager.init_app(app)
    login_manager.login_view = "login"

    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registro de los Blueprints
    from .public import public_bp
    app.register_blueprint(public_bp)

    #from .admin import admin_bp
    #app.register_blueprint(admin_bp)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)


    register_error_handlers(app)

    return app

def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404

    @app.errorhandler(401)
    def error_401_handler(e):
        return render_template('401.html'), 401