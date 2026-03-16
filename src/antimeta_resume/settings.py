from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Paths
    ROOT: Path = Path(__file__).resolve().parents[2]
    THEME: Path = ROOT / "theme"

settings = Settings()
