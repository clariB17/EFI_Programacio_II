import datetime
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db

class Libros(db.Model):
    # DEFINIMOS LA CLAVE PRIMARIA
    id = db.Column(db.Integer, primary_key=True)
    # SE FIJA LA RELACION ENTRE LA CLASE POST Y LA CLASE USER MEDIANTE EL ATRIBUTO user_id. 
    # ESTE ATRIBUTO ES UNA CLAVE FORANEA, QUE NOS SIRVE PARA REFERENCIAR AL USUARIO QUE ESCRIBIÓ EL POST.
    autor_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    title_slug = db.Column(db.String(256), unique=True, nullable=False)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan', order_by='asc(Comment.created)')

    def __repr__(self):
        return '<Post {self.title}>'

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
    def get_by_slug(slug):
        return Libros.query.filter_by(title_slug=slug).first()

    @staticmethod
    def get_by_id(id):
        return Libros.query.get(id)

    @staticmethod
    def get_all():
        return Libros.query.all()

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='SET NULL'))
    user_name = db.Column(db.String(256))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, content, user_id=None, user_name=user_name, post_id=None):
        self.content = content
        self.user_id = user_id
        self.user_name = user_name
        self.post_id = post_id

    def __repr__(self):
        return f'<Comment {self.content}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_post_id(post_id):
        return Comment.query.filter_by(post_id=post_id).all()