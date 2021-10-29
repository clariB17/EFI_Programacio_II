from collections import namedtuple
import datetime
from enum import auto
from typing import Coroutine
from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import backref, relationship

from app import db

class Libros(db.Model):
     # DEFINIMOS LA CLAVE PRIMARIA
    id = db.Column(db.Integer, primary_key=True)
    # SE FIJA LA RELACION ENTRE LA CLASE Libro Y LA CLASE USER MEDIANTE EL ATRIBUTO user_id. 
    # ESTE ATRIBUTO ES UNA CLAVE FORANEA, QUE NOS SIRVE PARA REFERENCIAR AL USUARIO QUE ESCRIBIÓ EL Libro.
    title = db.Column(db.String(256), nullable = False)
    precio = db.Column(db.Float(10.2), nullable = False)
    fecha_publicacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    ruta_foto = db.Column(db.String(150), nullable=True)
    ruta_libro = db.Column(db.String(150), nullable=False)

    #key
    id_genero = db.relationship('Genero', backref = 'libros', lazy=True, cascade='all, delete-orpan', order_by='asc(Genero.created)')
    id_autor = db.relationship('Autor', backref = 'libros', lazy=True, cascade='all, delete-orpan', order_by='asc(Autor.created)')
    id_idioma = db.relationship('Idioma', backref = 'libros', lazy=True, cascade='all, delete-orpan', order_by='asc(Idioma.created)')

    def __repr__(self):
        return f'<Libro {self.title}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.title_slug:
            self.title_slug = slugify(self.title)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1
                self.title_slug = f'{self.title_slug}-{count}'

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Libros.query.get(id)

    @staticmethod
    def get_all():
        return Libros.query.all()


# sobre el libro
class Genero():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Genero {self.name}'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id(id):
        return Genero.query.get(id)
    
    @staticmethod
    def get_all():
        return Genero.query.all()

class Puntuacion():
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    id_libro = db.relationship('Libro', backref = 'puntuacion', lazy=True, cascade='all, delete-orpan')

    def __init__(self, number, id_libro):
        self.number = number
        self.id_libro = id_libro

    def __repr__(self):
        return '<Genero {self.number}'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id_libro(id_libro):
        return Puntuacion.query.filter_by(id_libro=id_libro).all()

    @staticmethod
    def get_all():
        return Puntuacion.query.all()

class Autor():
    id = db.Column(db.Integer, primary_key = True)
    cuit = db.Column(db.String(11), nullable = True)
    name = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50), nullable = True)
    date_of_birth = db.Column(db.DateTime)
    id_pais = db.relationship('Pais', backref = 'autor', lazy=True, cascade='all, delete-orpan', order_by='asc(pais.created)')
    id_formacion = db.relationship('Formacion', backref = 'autor', lazy=True, cascade='all, delete-orpan', order_by='asc(Formacion.created)')
    rute_foto = db.Column(db.String(150), nullable = True)

    def __init__(self, name, id_pais):
        self.name = name
        self.id_pais = id_pais

    def __repr__(self):
        return '<autor {self.name}'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id():
        return Autor.query.get(id)

    @staticmethod
    def get_all():
        return Autor.query.all()

class Pais():
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<pais {self.name}'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id():
        return Pais.query.get(id)

    @staticmethod
    def get_all():
        return Puntuacion.query.all()

class Idioma():
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<idioma {self.name}'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id():
        return Idioma.query.get(id)

    @staticmethod
    def get_all():
        return Idioma.query.all()


# sobre usuario
from auth.models import User

class Deseados():
    id = db.Column(db.Integer, primary_key = True)
    id_libro = db.relationship('Libro', backref = 'deseados', lazy=True, cascade='all, delete-orpan')
    id_user = db.relationship('User', backref = 'deseados', lazy=True, cascade='all, delete-orpan')

    def __init__(self, name, id_user = None):
        self.name = name
        self.id_user = id_user

    def __repr__(self):
        return '<user {self.id_user}'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id_user(id_user):
        return Deseados.query.filter_by(id_user=id_user).all()

class Factura():
    id = db.Column(db.Integer, primary_key = True)
    id_user = db.relationship('User', backref = 'deseados', lazy=True, cascade='all, delete-orpan')
    fecha = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    monto = db.Column(db.Float(10.2), nullable = False)
    anulado = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, monto, id_user):
        self.monto = monto
        self.id_user = id_user

    def __repr__(self):
        return '<monto {self.monto}'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id_user(id_user):
        return Factura.query.filter_by(id_user=id_user).all()

    @staticmethod
    def get_all():
        return Factura.query.all()

class Detalle_factura():
    id = db.Column(db.Integer, primary_key = True)
    id_factura = db.relationship('Factura', backref = 'detalle_factura', lazy=True, cascade='all, delete-orpan')
    id_libro = db.relationship('Libro', backref = 'detalle_factura', lazy=True, cascade='all, delete-orpan')
    cantidad = db.Column(db.Integer)
    monto = db.Column(db.Float(10.2), nullable = False)
    anulado = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, monto, id_factura):
        self.monto = monto
        self.id_factura = id_factura

    def __repr__(self):
        return '<monto {self.monto}'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id_factura(id_factura):
        return Detalle_factura.query.filter_by(id_factura=id_factura).all()

    @staticmethod
    def get_all():
        return Detalle_factura.query.all()