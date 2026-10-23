"""
All helper functions are listed here
"""

import logging
import re
import json
from pathlib import Path

def load_file(file_path: str) -> str:
    """Load and return file contents as a string."""
    return Path(file_path).read_text().strip()

def get_logger(name: str) -> logging.Logger:
    """
    Sets up and returns a logger with a specified name
    Logs messages to the console with a specific format
    """
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s %(levelname)s: %(message)s]' 
    )

    return logging.getLogger(name)

def extract_text_from_json(text: str) -> dict:
    """
    Extract JSON from text string, returns null dict if empty
    """
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {}
    except json.JSONDecodeError:
        return {}
    