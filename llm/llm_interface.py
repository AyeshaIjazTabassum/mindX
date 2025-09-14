# mindx/llm/llm_interface.py
from abc import ABC, abstractmethod
from typing import Optional, Any, Dict

# ADDED: Import the new RateLimiter class
from .rate_limiter import RateLimiter

class LLMHandlerInterface(ABC): # pragma: no cover
    """
    Abstract Base Class for LLM handlers.
    Defines the common interface that specific LLM provider handlers must implement.
    """
    def __init__(self,
                 provider_name: str,
                 model_name_for_api: Optional[str],
                 api_key: Optional[str] = None,
                 base_url: Optional[str] = None,
                 rate_limiter: Optional[RateLimiter] = None,
                 **kwargs: Any):
        self.provider_name = provider_name
        self.model_name_for_api = model_name_for_api
        self.api_key = api_key
        self.base_url = base_url
        self.rate_limiter = rate_limiter


    @abstractmethod
    async def generate_text(
        self,
        prompt: str,
        model: str, # Model name/tag specific to the provider's API
        max_tokens: Optional[int] = 2048,
        temperature: Optional[float] = 0.7,
        json_mode: Optional[bool] = False, # Hint to try and get JSON output
        **kwargs: Any # Provider-specific parameters
    ) -> Optional[str]: 
        """
        Generates text based on the prompt using the specified model.
        
        Args:
            prompt: The input prompt.
            model: The specific model identifier for the provider's API.
            max_tokens: Maximum tokens to generate.
            temperature: Sampling temperature.
            json_mode: If true, attempt to instruct model for JSON output.
            kwargs: Additional provider-specific parameters.

        Returns:
            The generated text as a string, or an error string starting with "Error:",
            or None on critical failure.
        """
        pass
