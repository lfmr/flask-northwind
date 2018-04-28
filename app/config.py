import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):

    DEBUG = True
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_DB = 'northwind'
    MYSQL_DATABASE_USER= 'northwind'
    MYSQL_DATABASE_PASSWORD= 'northwind'

