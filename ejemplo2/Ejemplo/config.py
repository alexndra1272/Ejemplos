import os

# Configuraciones generales
class Config:
    SQLALCHEMY_DATABASE_URI : str = os.environ.get("DATABASE_URI")
    SECRET_KEY = os.environ.get("secret") 
    def __init__(self) -> None:
        pass

# Entorno de desarrollo
class ConfigDev(Config):
    FLASK_DEBUG=1
    SQLALCHEMY_DATABASE_URI : str = os.environ.get("DATABASE_URI_DEV")

# Entorno de produccion
class ConfigProd(Config):
    SQLALCHEMY_DATABASE_URI : str = os.environ.get("DATABASE_URI_PROD")

# Entorno de test
class ConfigTest(Config):
    def __init__(self) -> None:
        pass


config_env = {
    "dev" : ConfigDev,
    "prod" : ConfigProd,
    "test" : ConfigTest
}