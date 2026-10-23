from llm.prompt_library.prompts import generate_prompt

def build_prompt(message:str, strategy: str = "react") -> str:
    """
    Build a prompt for the user message based on selected strategy
    """
    if strategy == "react":
        return generate_prompt(message)

    else:
        raise NotImplementedError(f"{strategy} is not implemented")