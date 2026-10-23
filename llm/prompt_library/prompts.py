from utils import load_file
from pathlib import Path

PROMPT_DIR = Path(__file__).parent

def load_prompt(filename: str) -> str:
    """
    Loads prompts from the prompt directory
    """
    print(PROMPT_DIR)
    return load_file(PROMPT_DIR/filename)

def generate_prompt(user_input: str) -> str:
    """
    Generate a prompt for scam detection
    """
    #template = PROMPT
    template = load_prompt("react.md")
    return f"{template}\n\nUser Message:\n{user_input.strip()}"