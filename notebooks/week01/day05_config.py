from ai_engineer.config import Settings

s = Settings()
print(s.anthropic_api_key)
print(s.anthropic_api_key.get_secret_value())
print(s.max_concurrency, type(s.max_concurrency))
