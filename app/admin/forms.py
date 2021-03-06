# HEREDAMOS FLASKFORM
from flask_wtf import FlaskForm
# HEREDAMOS 4 COMPONENTES, CAJA DE TEXTO, BOTON SUBMIT, CAMPO PARA CLAVE y AREA DE TEXTO
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, DecimalField, FileField
from wtforms import validators
# HEREDAMOS VALIDADORES, DATO REQUERIDO, Username Y LARGO DE UN CAMPO
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField

from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import Genero, Autor, Idioma, Pais


class Libros_upload(FlaskForm): 
    titulo = StringField(label='Título', validators=[DataRequired(), Length(max=128)])
    ISBN = StringField(label='ISBN', validators=[DataRequired(), Length(max=128)])
    precio = DecimalField(label='Precio')
    libro = FileField(label='Adjuntar libro')
    imagen = FileField(label='Adjuntar imagen')
    genero = QuerySelectField(label='Genero', query_factory=Genero.get_all, get_label='nombre', allow_blank=True, validators=[DataRequired()])
    autor = QuerySelectField(label='Autor', query_factory=Autor.get_all, get_label='nombre', allow_blank=True, validators=[DataRequired()])
    idioma = QuerySelectField(label='Idioma', query_factory=Idioma.get_all, get_label='nombre', allow_blank=True, validators=[DataRequired()])
    submit = SubmitField(label='Guardar')

class Autores_upload(FlaskForm):
    nombre = StringField(label='Nombre', validators=[DataRequired(), Length(max=128)])
    apellido = StringField(label='Apellido', validators=[DataRequired(), Length(max=128)])
    fecha_de_nacimiento = DateField(label='fecha de nacimiento', format = '%Y-%m-%d', validators=(validators.DataRequired(),))
    imagen = FileField(label='Adjuntar imagen', validators=[DataRequired()])
    pais = QuerySelectField(label='Pais', query_factory=Pais.get_all, get_label='nombre', allow_blank=True, validators=[DataRequired()])
    submit = SubmitField(label='Guardar')



    
