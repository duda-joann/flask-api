import os
from pathlib import Path
#from dotenv import load_dotenv

base_dir = Path(__file__).resolve().parent
env_file = base_dir / '.env'
#load_dotenv(env_file)


class Config:
    DEBUG = True
    SQLALCHELMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}

