"""
Text utility functions for the Blog Generation System.
Provides text processing, cleaning, and analysis capabilities.
"""

import re
from typing import List, Optional
from ..utils.config import config


class TextUtils:
    """Utility class for text processing operations."""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean and normalize text by removing extra whitespace and special characters.
        
        Args:
            text: Input text to clean
            
        Returns:
            Cleaned text
        """
        if not text:
            return ""
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^\w\s\.\,\!\?\-\:]', '', text)
        return text.strip()
    
    @staticmethod
    def count_words(text: str) -> int:
        """
        Count the number of words in text.
        
        Args:
            text: Input text
            
        Returns:
            Word count
        """
        if not text:
            return 0
        words = text.split()
        return len(words)
    
    @staticmethod
    def truncate_text(text: str, max_words: int = None) -> str:
        """
        Truncate text to a maximum number of words.
        
        Args:
            text: Input text
            max_words: Maximum number of words (uses config if None)
            
        Returns:
            Truncated text
        """
        if max_words is None:
            max_words = config.MAX_RESEARCH_WORDS
            
        words = text.split()
        if len(words) <= max_words:
            return text
        
        truncated = ' '.join(words[:max_words])
        return truncated + "..."
    
    @staticmethod
    def extract_key_phrases(text: str, max_phrases: int = 10) -> List[str]:
        """
        Extract potential key phrases from text (simple implementation).
        
        Args:
            text: Input text
            max_phrases: Maximum number of phrases to extract
            
        Returns:
            List of key phrases
        """
        # Simple implementation - in a real system, you might use NLP libraries
        words = text.lower().split()
        # Filter for longer, potentially meaningful words
        key_words = [word for word in words if len(word) > 5 and word.isalpha()]
        return list(set(key_words))[:max_phrases]
    
    @staticmethod
    def format_sources(sources: List) -> str:
        """
        Format a list of research sources into a readable string.
        
        Args:
            sources: List of ResearchSource objects or similar
            
        Returns:
            Formatted sources string
        """
        if not sources:
            return "No sources available."
        
        formatted = []
        for i, source in enumerate(sources, 1):
            if hasattr(source, 'reference') and hasattr(source, 'source_type'):
                formatted.append(f"{i}. [{source.source_type.upper()}] {source.reference}")
            else:
                formatted.append(f"{i}. {str(source)}")
        
        return "\n".join(formatted)


# Create utility instance for easy import
text_utils = TextUtils()