import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """
    Base Configuration
    """
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY') or 's3cr37'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    @staticmethod
    def init_app(app):
        pass
    

class DevelopmentConfig(BaseConfig):
    """
    Development Configuration
    """
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or f"sqlite:///{os.path.join(basedir, 'asset.sqlite')}"

class TestingConfig(BaseConfig):
    """
    Testing Configuration
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')

class ProductionConfig(BaseConfig):
    """
    Base Configuration
    """
    pass

config = {
        'development' : DevelopmentConfig,
        'testing' : TestingConfig,
        'production' : ProductionConfig,

        'default' : DevelopmentConfig,
        }