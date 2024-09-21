import os
import sys

from pydantic import BaseModel
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict, YamlConfigSettingsSource

active_profile = os.getenv("ACTIVE_ENV", default="dev")
yaml_file = f'./config.{active_profile}.yaml'
print(os.getcwd())
print(sys.path)


# 定义应用程序配置模式
class AppConfig(BaseModel):
    host: str
    port: int
    loglevel: str


class DatabaseConfig(BaseModel):
    driver: str
    host: str
    port: int
    name: str
    user: str
    password: str


# 定义整个应用程序的配置
class Config(BaseSettings):

    model_config = SettingsConfigDict(
        yaml_file=yaml_file,
        yaml_file_encoding='utf-8'
    )

    app: AppConfig
    database: DatabaseConfig

    @classmethod
    def settings_customise_sources(
            cls,
            settings: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource, **kwargs
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            YamlConfigSettingsSource(settings),
        )


config = Config()
print(config)
