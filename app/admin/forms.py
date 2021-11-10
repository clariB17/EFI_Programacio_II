# HEREDAMOS FLASKFORM
from flask_wtf import FlaskForm
# HEREDAMOS 4 COMPONENTES, CAJA DE TEXTO, BOTON SUBMIT, CAMPO PARA CLAVE y AREA DE TEXTO
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, DecimalField, FileField
# HEREDAMOS VALIDADORES, DATO REQUERIDO, Username Y LARGO DE UN CAMPO
from wtforms.validators import DataRequired, Length


from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import Genero, Autor, Idioma

def get_genero():
    return Genero.get_all()

def get_autor():
    return Autor.get_all()

def get_idioma():
    return Idioma.get_all()

class Libros_upload(FlaskForm): 
    titulo = StringField(label='Título', validators=[DataRequired(), Length(max=128)])
    ISBN = StringField(validators=[DataRequired(), Length(max=128)])
    precio = DecimalField(label='Precio')
    libro = FileField(label='Adjuntar libro')
    imagen = FileField(label='Adjuntar imagen')
    genero = QuerySelectField(label='Genero', query_factory=get_genero, get_label='nombre', allow_blank=True)
    autor = QuerySelectField(label='Autor', query_factory=get_autor, get_label='nombre', allow_blank=True)
    idioma = QuerySelectField(label='Idioma', query_factory=get_idioma, get_label='nombre', allow_blank=True)
    submit = SubmitField(label='Guardar')







class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Enviar')

class UserAdminForm(FlaskForm):
    is_admin = BooleanField('Administrador')
    submit = SubmitField('Guardar')



    