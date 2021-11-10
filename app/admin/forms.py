# HEREDAMOS FLASKFORM
from os import name
from flask_wtf import FlaskForm
# HEREDAMOS 4 COMPONENTES, CAJA DE TEXTO, BOTON SUBMIT, CAMPO PARA CLAVE y AREA DE TEXTO
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.fields.core import DecimalField, FloatField, SelectField
from wtforms.fields.simple import FileField
# HEREDAMOS VALIDADORES, DATO REQUERIDO, EMAIL Y LARGO DE UN CAMPO
from wtforms.validators import DataRequired, Length



from app.models import Genero, Autor, Idioma



class Libros_upload(FlaskForm):
    # generos = Genero.get_all()
    # autores = Autor.get_all()
    # idiomas = Idioma.get_all()

    choices_genero = [123, '12sas']
    choices_autor = [123, '12sas']
    choices_idioma = [123, '12sas']

    # for genero in generos:
    #     choices_genero.append(genero.nombre())

    # for autor in autores:
    #     choices_autor.append(autor.nombre())

    # for idioma in idiomas:
    #     choices_idioma.append(idioma.nombre())
        
    titulo = StringField('Título', validators=[DataRequired(), Length(max=128)])
    ISBN = StringField(validators=[DataRequired(), Length(max=128)])
    precio = DecimalField('Precio')
    libro = FileField('Adjuntar libro')
    imagen = FileField('Adjuntar imagen')
    genero = SelectField('Genero', choices=choices_genero)
    autor = SelectField('Autor', choices=choices_autor)
    idioma = SelectField('Idioma', choices=choices_idioma)
    submit = SubmitField('Guardar')







class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Enviar')

class UserAdminForm(FlaskForm):
    is_admin = BooleanField('Administrador')
    submit = SubmitField('Guardar')



    