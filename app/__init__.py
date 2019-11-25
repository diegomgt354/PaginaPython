#al agregar el archivo __init_.py la carpera app sera un modulo
from flask import Flask

from flask_mail import Mail #pip install Flask-Mail
from flask_bootstrap import Bootstrap #pip install Flask-Bootstrap4
from flask_wtf.csrf import CSRFProtect #pip install Flask-WTF
from flask_sqlalchemy import SQLAlchemy #pip install Flask-SQLAlchemy

#pip install flask-login
from flask_login import LoginManager

app = Flask(__name__)

mail = Mail()
db = SQLAlchemy()
bootstrap = Bootstrap()
csrf = CSRFProtect()
login_manager = LoginManager()

from .views import page
from .models import User#nose porque si lo pongo mas arriba no funciona XD

def create_app(valor):
	app.config.from_object(valor)
	
	csrf.init_app(app)
	bootstrap.init_app(app)
	login_manager.init_app(app)
	
	#url a la cual se le redirige el usuarios cuando no se inicia sesion
	login_manager.login_view=".login" #url_for
	login_manager.login_message="Inicia sesión para acceder a esta página."

	mail.init_app(app)

	app.register_blueprint(page)

	with app.app_context():
		db.init_app(app)
		db.create_all()

	return app