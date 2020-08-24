class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/flask_contacts"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    Debug=True


class Testing(Config):
    pass

config = {
    "development": Development
}