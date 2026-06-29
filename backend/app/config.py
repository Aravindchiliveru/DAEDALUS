from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://daedalus:daedalus@localhost:5432/daedalus"
    cors_origins: str = "http://localhost:5173"


settings = Settings()
