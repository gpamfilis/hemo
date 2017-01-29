import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'cheese cake'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MONEYMAN_MAIL_SUBJECT_PREFIX = 'real'
    MONEYMAN_MAIL_SENDER = 'cheesecakes'
    MONEYMAN_ADMIN = 'hipidi' # os.environ.get('ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
            }