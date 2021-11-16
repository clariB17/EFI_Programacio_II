# HEREDAMOS FLASKFORM
from flask_wtf import FlaskForm
# HEREDAMOS 4 COMPONENTES, CAJA DE TEXTO, BOTON SUBMIT, CAMPO PARA CLAVE y AREA DE TEXTO
from wtforms import StringField, SubmitField, PasswordField, BooleanField
# HEREDAMOS VALIDADORES, DATO REQUERIDO, Username Y LARGO DE UN CAMPO
from wtforms.validators import DataRequired, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired(), Length(max=64)])
    submit = SubmitField('Registrar')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')
