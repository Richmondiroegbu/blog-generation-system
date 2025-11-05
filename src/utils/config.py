"""
Configuration module for the Blog Generation System.
Handles environment variables, API configuration, and global settings.
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for managing application settings."""
    
    # Groq API Configuration
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    GROQ_MODEL: str = "llama-3.1-8b-instant"
    GROQ_TEMPERATURE: float = 0.3
    GROQ_MAX_TOKENS: int = 4000
    
    # Agent Configuration
    MAX_RESEARCH_WORDS: int = 800
    MAX_BLOG_LENGTH: int = 1500
    
    # Tool Configuration
    WIKIPEDIA_MAX_RESULTS: int = 2
    SEARCH_MAX_RESULTS: int = 2
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate configuration."""
        if not cls.GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY not found. Please set it in your .env file."
            )
        return True

    @classmethod
    def get_groq_config(cls) -> dict:
        """Get Groq configuration."""
        return {
            "model": cls.GROQ_MODEL,
            "temperature": cls.GROQ_TEMPERATURE,
            "max_tokens": cls.GROQ_MAX_TOKENS,
        }

# Create config instance
config = Config()