#pip install WTForms
from wtforms import Form#pip install WTForms
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms import validators
from wtforms.fields.html5 import EmailField

from .models import User, Task

def diego_validator(form, field):
	if field.data == "diego" or field.data == "Diego":
		raise validators.ValidationError("El username diego no es permitido")

class LoginForm(Form):
	username = StringField("Username",[
			validators.length(min=4, max=50, message="El campo debe tener entre 4 y 50 caracteres de longitud.")
		])
	password = PasswordField("Password",[
			validators.Required(message="El Password es requerido.")
		])

class RegisterForm(Form):
	username = StringField("Username",[
			validators.length(min=4, max=50),
			diego_validator
		])
	email = EmailField("Email",[
			validators.length(min=6, max=100),
			validators.Required(message="El email es requerido."),
			validators.Email(message="Ingrese un correo Valido.")
		])
	password = PasswordField("Password",[
			validators.Required("El password es requerido."),
			validators.EqualTo("confirm_password",message="El password no coincide.")
		])
	confirm_password = PasswordField("Confirmar Email")
	accept = BooleanField("",[validators.DataRequired()])

	def validate_username(self, username):
		if User.get_by_username(username.data):
			raise validators.ValidationError("El username ya se encuentra en uso")

	def validate_email(self, email):
		if User.get_by_email(email.data):
			raise validators.ValidationError("El email ya se encuentra en uso")

	#sobreescribimos la funcion validate
	def validate(self):
		if not Form.validate(self):
			return False

		if len(self.password.data) < 3:
			self.password.errors.append("El password es demasiado corto")
			return False

		return True

class TaskForm(Form):
	title = StringField("titulo",[
			validators.length(min=4, max=50, message="Titulo Fuera de rango."),
			validators.DataRequired(message="El titulo es requerido.")
		])
	description = TextAreaField("Descripción",[
			validators.DataRequired(message="La descripción es requerida.")
		],render_kw={"rows": 10})