from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(Path(__file__).resolve().parent.parent / ".env", override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")