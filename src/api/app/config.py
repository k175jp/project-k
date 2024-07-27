import os
import pathlib

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

root = pathlib.Path(__file__).parent
env_file = root / '.env'

DB_USER = os.getenv("MYSQL_USER", "")
DB_PASS = os.getenv("MYSQL_PASSWORD", "")
DB_NAME = os.getenv("MYSQL_DATABASE", "")

from logging import getLogger, StreamHandler
logger = getLogger(__name__)
logger.addHandler(StreamHandler())
logger.setLevel("INFO")

logger.info(f"{DB_USER =} {DB_PASS = } {DB_NAME = }")


class Settings(BaseSettings):
    project_root: pathlib.Path = root
    secret: str = ""
    db_uri: str = f"mysql+pymysql://{DB_USER}:{DB_PASS}@mysql/{DB_NAME}?charset=utf8"
    token_url: str = "/auth/login"
    model_config = ConfigDict(env_file='.env')


Config = Settings(_env_file=env_file)
