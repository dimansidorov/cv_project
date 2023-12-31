import os

from dotenv import load_dotenv

load_dotenv()

'''SECRET KEY'''
SECRET_KEY = os.environ.get('SECRET_KEY')

'''DATABASE'''
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

'''AUTH'''
COOKIE_LIFETIME = 3600
JWT_LIFETIME = 3600
