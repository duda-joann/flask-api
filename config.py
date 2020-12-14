import os
from pathlib import Path
from dotenv import load_dotenv

base_dir = Path(__file__).resolve().parent
env_file = base_dir / '.env'
load_dotenv(env_file)

class Config:
    DEBUG = True
    SQLALCHELMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DB_FILE_PATH = base_dir / 'database_creation'/ 'artists.db'
    SQLALCHELMY_DATABASE_URI = f'sqlite:///{DB_FILE_PATH}'
    DEBUG = True
    TESTING = True



class TestingConfig(Config):
    DB_FILE_PATH = base_dir /'tests'/ 'test.db'
    SQLALCHELMY_DATABASE_URI = f'sqlite:///{DB_FILE_PATH}'
    DEBUG = True
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
