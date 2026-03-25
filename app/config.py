from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """
    Configuración de la aplicación.
    """
    APP_NAME: str = "FastAPI CRUD"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "API CRUD con FastAPI"

    DATABASE_URL: str = "postgresql://ivan:2002@localhost:5432/tareas_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Config()
