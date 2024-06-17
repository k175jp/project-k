import pathlib

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

root = pathlib.Path(__file__).parent
env_file = root / '.env'


class Settings(BaseSettings):
    project_root: pathlib.Path = root
    secret: str = ""
    db_uri: str = "mysql+pymysql://project_k:project_k@mysql/project_k?charset=utf8"
    token_url: str = "/auth/login"
    model_config = ConfigDict(env_file='.env')


Config = Settings(_env_file=env_file)
