class Config:
    SECRET_KEY='mi_clave_secreta_123'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
    }