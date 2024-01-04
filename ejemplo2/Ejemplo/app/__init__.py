from flask import Flask
from config import config_env
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from dotenv import load_dotenv


load_dotenv()

db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config_env[config_name])

    db.init_app(app)

    migrate = Migrate(app, db)

    # Importar el blueprint
    from .auth import auth as auth_blueprint

    # Registrar un blueprint
    app.register_blueprint(auth_blueprint)
    return app



app = create_app("dev")

if __name__ == "__main__":
    app.run()