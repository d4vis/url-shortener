from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = os.environ.get('PORT', 8000)
    database_url: str = 'postgresql://gnxxyfjvnoitpf:2a61b54db5ebfa2a2b8bfbec4c6ba64921d7ff940110ee5352eee94dd5f72bb3@ec2-54-228-99-58.eu-west-1.compute.amazonaws.com:5432/df03soj2omvom5'


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
