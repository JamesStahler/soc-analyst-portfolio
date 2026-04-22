from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ATS Job Matcher API"
    api_prefix: str = "/api/v1"

    database_url: str
    redis_url: str

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"

    search_provider: str = "bing"
    bing_api_key: str = ""
    bing_api_endpoint: str = "https://api.bing.microsoft.com/v7.0/search"
    serpapi_api_key: str = ""

    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_price_pro_monthly: str = ""
    stripe_price_payg: str = ""

    match_threshold: int = 60
    max_results: int = 20

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
