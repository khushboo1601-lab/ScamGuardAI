from typing import List,Dict,Any
from .executor import LLMExecutor
from .parser import OutputParser
from .builder import build_prompt
from utils import get_logger

logger = get_logger(__name__)

class ScamDetector:
    """
    This is the main class for scam detection
    """

    def __init__(self,strategy :str ="react") -> None:
        """
        Initiliased the scam detection pipeline
        """
        self.executor = LLMExecutor()
        self.parser = OutputParser()
        self.strategy = strategy
        logger.info(f"Initialised detector class with strategy: {self.strategy}")

    def detect(self,message:str) -> Dict[str,Any]:
        """
        Runs the main detection pipeline
        """
        logger.info("Started the main scam detection class")
        try:
            prompt = build_prompt(message,self.strategy)
            raw_output = self.executor.execute(prompt)
            parsed_output = self.parser.parse_llm_output(raw_output)

            logger.info(f"Detection is successful!")
            return parsed_output

        except Exception as e:
            logger.error(f"Detection pipeline failed: {e}")