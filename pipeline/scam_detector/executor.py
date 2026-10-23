from typing import Optional
from llm.prompt_library.client import LLMClient
from utils import get_logger

logger = get_logger(__name__)

class LLMExecutor:
    """
    Executes prompts using LLM Client.
    """

    def __init__(self, model: Optional[str] = None) -> None:
        """
        Initialized LLMExecutor

        Args:
            model: Optional argument for specifying the model.
        """
        self.llm = LLMClient(model) if model else LLMClient()
        logger.info("Initialized LLMExecutor.")

    def execute(self, prompt: str) -> str:
        """
        Executes the prompt using the LLM Client and returns the raw response

        Args
            - prompt: The formatted prompt that should be consumed by the LLM

        Returns
            Raw LLM response
        
        Raises
            Exception: When LLM execution fails
        """
        logger.info(f"Executing LLM with the final prompt.")
        try:
            response = self.llm.call(prompt)
            logger.info("LLM execution is successful.")

            return response

        except Exception as e:
            logger.error(f"LLM Execution failed: {str(e)}")
            raise e