#src/models/blog_models.py

"""
Data models for the Blog Generation System.
"""

from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field, ConfigDict


class ResearchSource(BaseModel):
    """Model representing a single research source."""
    content: str = Field(description="The actual content/text from the source")
    source_type: str = Field(description="Type of source (wikipedia, web_search, etc.)")
    reference: str = Field(description="Reference information (URL, title, query)")
    relevance_score: Optional[float] = Field(default=None, description="How relevant this source is to the topic")


class ResearchResult(BaseModel):
    """Model representing the complete research findings."""
    topic: str = Field(description="The original research topic")
    summary: str = Field(description="Synthesized research summary")
    key_points: List[str] = Field(description="List of key findings/points")
    sources: List[ResearchSource] = Field(description="List of research sources used")
    research_queries: List[str] = Field(description="Search queries used during research")


class BlogSection(BaseModel):
    """Model representing a single section of the blog."""
    heading: str = Field(description="Section heading")
    content: str = Field(description="Section content")
    word_count: int = Field(description="Approximate word count for this section")


class BlogOutline(BaseModel):
    """Model representing the complete blog outline."""
    topic: str = Field(description="The blog topic")
    title: str = Field(description="Proposed blog title/heading")
    introduction: BlogSection = Field(description="Introduction section")
    content_sections: List[BlogSection] = Field(description="Main content sections")
    conclusion: BlogSection = Field(description="Conclusion/summary section")
    target_audience: str = Field(description="Intended target audience")
    tone: str = Field(description="Desired tone (professional, casual, technical, etc.)")


class GeneratedBlog(BaseModel):
    """Model representing the final generated blog."""
    outline: BlogOutline = Field(description="The outline used for generation")
    content: str = Field(description="Full blog content in markdown format")
    word_count: int = Field(description="Total word count")
    research_sources: List[ResearchSource] = Field(description="Sources used in the blog")
    generation_metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Metadata about the generation process"
    )


class AgentResponse(BaseModel):
    """Generic model for agent responses with status tracking."""
    model_config = ConfigDict(extra='forbid')  # Prevent extra fields
    
    success: bool = Field(description="Whether the operation was successful")
    data: Optional[Union[ResearchResult, BlogOutline, GeneratedBlog]] = Field(default=None, description="The main response data")
    error_message: Optional[str] = Field(default=None, description="Error message if operation failed")
    processing_time: Optional[float] = Field(default=None, description="Time taken for processing in seconds")


# Type aliases for clearer function signatures
BlogTopic = str
ResearchQuery = str














