import os

BASE_DIR = os.path.abspath(os.path.dirname(__name__))

class Config:
    SECRET_KEY = 'uma chave qualquer'
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')

    @staticmethod
    def init_app(app):
        pass