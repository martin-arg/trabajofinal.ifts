from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from extensiones import db, ma
import models.usuarios

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clubsocial-python.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db.init_app(app)
ma.init_app(app)

# Configurar login
login_manager = LoginManager()
login_manager.login_view = 'auth.sign-up'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return models.usuarios.Usuarios.query.get(user_id)

# Registrar rutas
import routes.principal
import routes.profile

app.register_blueprint(routes.principal.principal)
app.register_blueprint(routes.profile.profile)

if __name__ == '__main__':
    app.run(port=5000, debug=True)