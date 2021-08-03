import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-dev.db".format(basedir)


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-prod.db".format(basedir)


def get_config(env='dev'):
    if env == 'prod':
        return ProductionConfig
    else:
        return DevelopmentConfig
