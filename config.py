class Config:
    SECRET_KEY = 'mi_clave_secreta_123'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'ROOT'
    MYSQL_DB = 'tienda'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
