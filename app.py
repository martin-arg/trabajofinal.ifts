from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://root@localhost/clubsocial'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://axubygqajqrehm:be2bb89c707bd6cef04b73858ac7705aba7e653cbd7db769a1f40aa872a3820e@ec2-54-152-28-9.compute-1.amazonaws.com:5432/dcomknu5qjbgip'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.sign-up'
login_manager.init_app(app)

import models.usuarios



@login_manager.user_loader
def load_user(user_id):
    return models.usuarios.Usuarios.query.get(user_id)


import routes.principal
import routes.auth
import routes.profile

app.register_blueprint(routes.principal.principal)
app.register_blueprint(routes.auth.auth)
app.register_blueprint(routes.profile.profile)

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
