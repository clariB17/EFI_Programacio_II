import datetime
from enum import unique
from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db

class Libro(db.Model):
     # DEFINIMOS LA CLAVE PRIMARIA
    id = db.Column(db.Integer, primary_key=True)
    # SE FIJA LA RELACION ENTRE LA CLASE Libro Y LA CLASE USER MEDIANTE EL ATRIBUTO user_id. 
    # ESTE ATRIBUTO ES UNA CLAVE FORANEA, QUE NOS SIRVE PARA REFERENCIAR AL USUARIO QUE ESCRIBIÓ EL Libro.
    titulo = db.Column(db.String(256), nullable = False)
    ISBN = db.Column(db.String(50), nullable = False, unique=True)
    precio = db.Column(db.Float(10.2), nullable = False)
    fecha_publicacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    ruta_foto = db.Column(db.String(150), nullable=True)
    ruta_libro = db.Column(db.String(150), nullable=False)

    #key
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id'), nullable=False)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)
    id_idioma = db.Column(db.Integer, db.ForeignKey('idioma.id'), nullable=False)

    deseados = db.relationship('Deseados', backref = 'libro', lazy=True)
    puntuacion = db.relationship('Puntuacion', backref = 'libro', lazy=True)
    detalle_factura = db.relationship('Detalle_factura', backref = 'libro', lazy=True)


    def __repr__(self):
        return f'<Libro {self.titulo}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Libro.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Libro.query.filter_by(ISBN=name).first() 

    @staticmethod
    def get_all():
        return Libro.query.all()
    
    @staticmethod
    def get_last():
        if len(Libro.get_all()) >= 3:
            obj = Libro.query.all()
            return obj[-3] , obj[-2], obj[-1]
        return Libro.get_all()


# sobre el libro
class Genero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(3), nullable=False)

    # key
    libro = db.relationship('Libro', backref = 'genero', lazy=True)

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '<Genero {self.nombre}'

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
    def get_by_name(name):
        return Genero.query.filter_by(nombre=name).first()  

    @staticmethod
    def get_all():
        return Genero.query.all()

class Puntuacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)

    # key
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    
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
    nombre = db.Column(db.String(50), nullable = False)
    apellido = db.Column(db.String(50), nullable = True)
    fecha_de_nacimiento = db.Column(db.DateTime)
    ruta_foto = db.Column(db.String(150), nullable = True)

    # key
    libro = db.relationship('Libro', backref = 'autor', lazy=True)

    id_pais = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)


    def __repr__(self):
        return '<autor {self.nombre}'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id(id):
        return Autor.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return Autor.query.filter_by(nombre=name).first() 

    @staticmethod
    def get_all():
        return Autor.query.all()

class Pais(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False) 
    codigo = db.Column(db.String(5), nullable=False)
    continente = db.Column(db.String(100), nullable=False)

    # key
    autor = db.relationship('Autor', backref = 'pais', lazy=True)

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '<pais {self.nombre}'

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
    def get_by_name(name):
        return Pais.query.filter_by(nombre=name).first() 

    @staticmethod
    def get_all():
        return Pais.query.all()

class Idioma(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    codigo = db.Column(db.String(5), nullable=False)

    # key
    libro = db.relationship('Libro', backref = 'idioma', lazy=True)

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '<idioma {self.nombre}'

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
    def get_by_name(name):
        return Idioma.query.filter_by(nombre=name).first() 

    @staticmethod
    def get_all():
        return Idioma.query.all()


# sobre usuario

class Deseados(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    # key
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, nombre, id_user = None):
        self.nombre = nombre
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
    
    @staticmethod
    def get_liked(id_user, id_libro):
        return Deseados.query.filter_by(id_user=id_user, id_libro=id_libro).first()

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
    anulado = db.Column(db.Boolean, nullable=False, default=0)

    # key
    id_factura = db.Column(db.Integer, db.ForeignKey('factura.id'), nullable=False)
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)

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
