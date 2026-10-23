from typing import Dict,Any
from utils import get_logger, extract_text_from_json

logger = get_logger(__name__)

class OutputParser():
    def parse_llm_output(self, llm_output:str) -> Dict[str,Any]:
        """
        Extracts and parse JSON structure from the LLM Output.
        args:
        llm_output: Raw string output from the llm.

    Returns:
        Dictionary that contains result from the LLM output.
        - label: str -> Classification result (Scam | No Scam | uncertain)
        - reasoning: str -> Analysis of the classification.
        - intent: str -> Intent of the message sender.
        - risk_factors: List[str] -> List of identified red flags in the message.
    """
        logger.info("Begin output parsing")
        parsed_json = extract_text_from_json(llm_output)

        if parsed_json:
            logger.info("Successfully parsed the LLM output to json")
            return parsed_json

        else:
            logger.warning("No JSON found in the LLM output")
            fallback_results = {
            "label" : "Uncertain",
            "reasoning" : "Could not parse AI response",
            "intent" : "Unknown",
            "risk_factors" : ["Parsing error"]
        }
            return fallback_results