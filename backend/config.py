import os

class Config:
    # PostgreSQL connection details
    POSTGRES_USER = os.environ.get('USERNAME')
    POSTGRES_PASSWORD = os.environ.get('PASSWORD')
    POSTGRES_HOST = os.environ.get('HOST')
    POSTGRES_PORT = os.environ.get('PORT')
    POSTGRES_DB = os.environ.get('DB')

    # Flask secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

# Create an instance of the configuration
config = Config()
