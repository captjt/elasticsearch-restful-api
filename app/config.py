import os


class BaseConfig(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    ERROR_404_HELP = False
    # Be sure to have a SECRET_KEY environment variable in production
    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b',
    )


class ProductionConfig(BaseConfig):
    """Production configuration."""
    ENV = 'production'
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    ENV = 'development'
    DEBUG = True
