from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = r'C:\\Samples\\test1\\01_quickstart\\.env'
        env_file_encoding = 'utf-8'


config = Settings()
