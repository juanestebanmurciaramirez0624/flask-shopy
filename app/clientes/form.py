from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import  InputRequired, Email
 

class RegistrarClientesForm():
    username = StringField("Digite el nombre del cliente:", validators = [InputRequired(message = "Nombre del cliente requerido")])
    password = StringField("Digite la contraseña del cliente:", validators = [InputRequired(message = "Contraeseña del cliente requerido")])
    email = StringField("Digite el email del cliente:", validators = [InputRequired(message = "Email del cliente requerido"),Email("Debe ser email pendejo")])
    
class NewClientesForm(FlaskForm, RegistrarClientesForm):
    submit = SubmitField("Guardar")

class EditClientesForm(FlaskForm, RegistrarClientesForm):
    submit = SubmitField("Actualizar")