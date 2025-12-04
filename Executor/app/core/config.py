import logging
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    API_PREFIX: str
    BASE_DIR: str = Path(__file__).resolve().parents[2].as_posix()

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env", extra="ignore")


settings = Settings()
