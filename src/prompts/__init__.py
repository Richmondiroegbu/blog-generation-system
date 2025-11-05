"""
Prompts package for Blog Generation System.
LLM prompt templates for all agents.
"""

from .research_prompts import ResearchPrompts, research_prompts
from .outline_prompts import OutlinePrompts, outline_prompts
from .writing_prompts import WritingPrompts, writing_prompts

__all__ = [
    "ResearchPrompts",
    "research_prompts",
    "OutlinePrompts", 
    "outline_prompts",
    "WritingPrompts",
    "writing_prompts"
]