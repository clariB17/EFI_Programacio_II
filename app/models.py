import datetime
from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError

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
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id'), nullable=False)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)
    id_idioma = db.Column(db.Integer, db.ForeignKey('idioma.id'), nullable=False)

    deseados = db.relationship('Deseados', backref = 'libros', lazy=True)
    puntuacion = db.relationship('Puntuacion', backref = 'libros', lazy=True)
    detalle_factura = db.relationship('Detalle_factura', backref = 'libros', lazy=True)

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
class Genero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # key
    libros = db.relationship('Libros', backref = 'genero', lazy=True,cascade='all, delete-orphan', order_by='asc(Genero.created)')

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

class Puntuacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)

    # key
    id_libros = db.Column(db.Integer, db.ForeignKey('libros.id'), nullable=False)
    
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

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cuit = db.Column(db.String(11), nullable = True)
    name = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50), nullable = True)
    date_of_birth = db.Column(db.DateTime)
    formacion = db.Column(db.String(100), nullable = True)
    rute_foto = db.Column(db.String(150), nullable = True)

    # key
    libros = db.relationship('Libros', backref = 'autor', lazy=True, order_by='asc(Autor.created)')

    id_pais = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)

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

class Pais(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)

    # key
    pais = db.relationship('Autor', backref = 'pais', lazy=True, order_by='asc(pais.created)')

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

class Idioma(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)

    # key
    libros = db.relationship('Libros', backref = 'idioma', lazy=True, order_by='asc(Idioma.created)')

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
from app.auth.models import User

class Deseados(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    # key
    id_libros = db.Column(db.Integer, db.ForeignKey('libros.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

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

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    monto = db.Column(db.Float(10.2), nullable = False)
    anulado = db.Column(db.Boolean, nullable=False, default=False)

    # key
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    detalle_factura = db.relationship('Detalle_factura', backref = 'factura', lazy=True)

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

class Detalle_factura(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cantidad = db.Column(db.Integer)
    monto = db.Column(db.Float(10.2), nullable = False)
    anulado = db.Column(db.Boolean, nullable=False, default=False)

    # key
    id_factura = db.Column(db.Integer, db.ForeignKey('factura.id'), nullable=False)
    id_libros = db.Column(db.Integer, db.ForeignKey('libros.id'), nullable=False)

    libro_actual = db.relationship('Libro_actual', backref = 'detalle_factura', lazy=True)

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

class Libro_actual(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    num_pagina = db.Column(db.Integer)

    # key
    id_detalle_factura = db.Column(db.Integer, db.ForeignKey('detalle_factura.id'), nullable=False)

    def __init__(self, num_pagina, id_detalle):
        self.num_pagina = num_pagina
        self.id_detalle = id_detalle

    def __repr__(self):
        return '<num_pagina {self.num_pagina}'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id():
        return Libro_actual.query.get(id)

    @staticmethod
    def get_all():
        return Libro_actual.query.all()
