from decouple import config #pip install python-decouple

class Config:#para configuraciones globales
	SECRET_KEY = 'LoqueNoTeImaginas123'

class DevelopmentConfig(Config):#para configuraciones especificas
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:abcdario@localhost/proyectoWeb'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = "aprendiendo.python.pro@gmail.com"
	MAIL_PASSWORD = config("MAIL_PASSWORD")

config={
	"Development":DevelopmentConfig,
	"default":DevelopmentConfig
}

#1.-sudo apt-get install python-dev default-libmysqlclient-dev
#2.-pip install mysqlclient
