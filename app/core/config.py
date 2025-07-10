from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = "development"

    postgres_server: str
    postgres_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str
    database_url: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
