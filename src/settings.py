from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME: str = "Salesforce/codegen-350M-mono"
    MAX_LENGTH: int = 256
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    LOG_LEVEL: str = "info"

settings = Settings()
