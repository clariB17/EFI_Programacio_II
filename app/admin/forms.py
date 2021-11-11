# HEREDAMOS FLASKFORM
from flask_wtf import FlaskForm
# HEREDAMOS 4 COMPONENTES, CAJA DE TEXTO, BOTON SUBMIT, CAMPO PARA CLAVE y AREA DE TEXTO
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, DecimalField, FileField, DateField
# HEREDAMOS VALIDADORES, DATO REQUERIDO, Username Y LARGO DE UN CAMPO
from wtforms.validators import DataRequired, Length


from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import Genero, Autor, Idioma, Libro, Pais


class Libros_upload(FlaskForm): 
    titulo = StringField(label='Título', validators=[DataRequired(), Length(max=128)])
    ISBN = StringField(label='ISBN', validators=[DataRequired(), Length(max=128)])
    precio = DecimalField(label='Precio')
    libro = FileField(label='Adjuntar libro')
    imagen = FileField(label='Adjuntar imagen')
    genero = QuerySelectField(label='Genero', query_factory=Genero.get_all, get_label='nombre', allow_blank=True)
    autor = QuerySelectField(label='Autor', query_factory=Autor.get_all, get_label='nombre', allow_blank=True)
    idioma = QuerySelectField(label='Idioma', query_factory=Idioma.get_all, get_label='nombre', allow_blank=True)
    submit = SubmitField(label='Guardar')

class Autores_upload(FlaskForm):
    nombre = StringField(label='Nombre', validators=[DataRequired(), Length(max=128)])
    apellido = StringField(label='Apellido', validators=[DataRequired(), Length(max=128)])
    fecha_de_nacimiento = DateField(label='fecha de nacimiento', )
    imagen = FileField(label='Adjuntar imagen')
    pais = QuerySelectField(label='Pais', query_factory=Pais.get_all, get_label='nombre', allow_blank=True)
    submit = SubmitField(label='Guardar')

class Recomendado:
    libro = QuerySelectField(label='Seleccione libro', query_factory=Libro.get_all, get_label='nombre', allow_blank=True)
    submit = SubmitField(label='Guardar')




############################################################
class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Enviar')

class UserAdminForm(FlaskForm):
    is_admin = BooleanField('Administrador')
    submit = SubmitField('Guardar')



    