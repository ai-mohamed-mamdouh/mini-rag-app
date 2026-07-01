from src.helpers.settings import get_settings
import os
from pathlib import Path

class BaseController :
    def __init__(self) :
        self.settings = get_settings()

        self.base_dir = Path(__file__).resolve().parents[2]
        self.files_dir = self.base_dir / "assets" / "files"

        self.files_dir.mkdir(parents=True, exist_ok=True)