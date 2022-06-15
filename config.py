# -*- coding: utf-8 -*-

print('Config Loading....')

class Config(object):
    DEBUG = True
    SECRET_KEY = 'SECRET_KEY'
    # SQLALCHEMY_DATABASE_URI = None

class ProductionConfig(Config):
    sql_alchemy_conn = 'postgresql://postgres:32167@localhost:5432/sber_atr'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:32167@localhost:5432/sber_atr'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Database settings:
# SQLALCHEMY_DATABASE_URI = None
# SQLALCHEMY_TRACK_MODIFICATIONS = False

# WTF_CSRF_ENABLED = False


# ----- Postgres -----
# user_login = None
# user_pass = None