from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail



configuration_params = {
    "gmail-user": "your-email@gmail.com",
    "gmail-password": "gmailpassword",
    "about_text": "Hi my name is harry and I create programming tutorials and I am a good boy",
    "no_of_posts": 3,
    "login_image": "login.svg",
    "admin_user": "harry",
    "admin_password": "subscribenow",
    "admin_id": "administrator",
    "upload_location": "C:\\Users\\Haris\\PycharmProjects\\Flask-tut\\static"
}



# importo i parametri di configurazione che ho settato

# creo un'istanza della mia applicazione flask
app = Flask(__name__)



# configuro la chiave segreta che serve per gestire la sessione degli utenti loggati
app.secret_key = 'super-secret-key'

# configuro il server mail per poter consentire agli utenti di inviarmi una mail attraverso la sezione contacts
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = configuration_params['gmail-user'],
    MAIL_PASSWORD = configuration_params['gmail-password']
)
mail = Mail(app)


# configuro il database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"


db = SQLAlchemy(app)
db.init_app(app)
from core.models.postsModel import Post
from core.models.userModel import User
from core.models.contactsModel import Contacts
db.create_all()

migrate = Migrate(app, db)


