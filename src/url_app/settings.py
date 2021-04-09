from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = os.environ.get('PORT', 8000)
    database_url: str = os.environ.get('SQLALCHEMY_DATABASE_URI')


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
