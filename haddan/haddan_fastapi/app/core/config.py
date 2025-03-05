from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str
    db_name: str
    db_host: str
    db_port: int

    class Config:
        env_file = '.env'


settings = Settings()
