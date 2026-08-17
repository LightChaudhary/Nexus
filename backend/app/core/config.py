from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    It is a central configuration system, it allows for:
    - Fast updates: Change a setting once, and all apps see it right away.
    - Better Security: Keep passworcs and keys hidden away in a secure vault.
    - No Downtime: Update live apps without needing to restart them.
    - Fewer Errors: Stop making manual edits on different servers.
    """

    PROJECT_NAME: str = "Nexus"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "local"
    API_KEY_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    # It tells Pydantic Settings how configuration loading should behave.
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra="ignore",
    )

settings = Settings()
