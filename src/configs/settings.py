from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file= ".env"
    )

    OLTP_HOST: str | None=None
    OLTP_PORT: int | None=None
    OLTP_USER: str | None=None
    OLTP_PASSWORD: str | None=None
    OLTP_DB: str | None=None
    OLTP_SCHEMA: str | None=None

    DW_HOST: str | None=None
    DW_PORT: int | None=None
    DW_USER: str | None=None
    DW_PASSWORD: str | None=None
    DW_DB: str | None=None
    DW_SCHEMA: str | None=None

    @property
    def OLTP_URL(self):
        return f"postgresql://{self.OLTP_USER}:{self.OLTP_PASSWORD}@{self.OLTP_HOST}:{self.OLTP_PORT}/{self.OLTP_DB}"
    @property
    def DW_URL(self):
        return f"postgresql://{self.DW_USER}:{self.DW_PASSWORD}@{self.DW_HOST}:{self.DW_PORT}/{self.DW_DB}"

@lru_cache
def get_settings() -> Settings:
    return Settings()