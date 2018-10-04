import os

class Config(object):
    """Parent Configuration Class"""
    DEBUG = False
    SECRET_KEY = 'mysecret'

class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for testing with a separate test database"""
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production"""
    DEBUG = False
    TESTING = False



app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}