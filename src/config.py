from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class AppConfig:
    """Central configuration for the Streamlit application."""

    openai_models: List[str] = field(
        default_factory=lambda: ["gpt-4o", "gpt-4.1", "gpt-5"]
    )
    default_model: str = "gpt-4o"
    max_tokens: int = 1500
    default_temperature: float = 0.7


APP_CONFIG = AppConfig()

