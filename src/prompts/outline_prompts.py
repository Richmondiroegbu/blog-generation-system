"""
Prompt templates for the Outline Agent.
Designed to guide the LLM in creating well-structured blog outlines.
"""

from langchain_core.prompts import PromptTemplate
from ..models.blog_models import BlogOutline


class OutlinePrompts:
    """Prompt templates for outline generation."""
    
    @property
    def blog_outline_prompt(self) -> PromptTemplate:
        """
        Prompt for generating a comprehensive blog outline from research.
        """
        return PromptTemplate(
            input_variables=["topic", "research_summary", "key_points", "current_date"],
            template="""You are an expert content strategist. Create a detailed blog outline based on the research provided.

BLOG TOPIC: {topic}
CURRENT DATE: {current_date}

RESEARCH SUMMARY:
{research_summary}

KEY POINTS TO COVER:
{key_points}

BLOG STRUCTURE REQUIREMENTS:
1. Heading: Clear, engaging title that captures the essence
2. Introduction: Hook readers and explain why this topic matters
3. Content: 3-5 main sections with subpoints, covering the key research findings
4. Summary: Conclude with main takeaways and potential future developments

CONTENT GUIDELINES:
- Ensure logical flow from introduction to conclusion
- Each section should build upon the previous one
- Include specific examples and data points from the research
- Consider the target audience: educated general readers
- Tone: Professional yet accessible

OUTLINE FORMAT:
Return a structured outline with:
- Main heading/title
- Introduction section with bullet points
- 3-5 main content sections, each with:
  * Section heading
  * 3-4 key subpoints or topics to cover
- Conclusion section with main takeaways

BLOG OUTLINE:"""
        )
    
    @property
    def outline_refinement_prompt(self) -> PromptTemplate:
        """
        Prompt for refining an existing outline based on additional research.
        """
        return PromptTemplate(
            input_variables=["initial_outline", "additional_research", "topic"],
            template="""Refine and improve the following blog outline by incorporating additional research findings.

TOPIC: {topic}

INITIAL OUTLINE:
{initial_outline}

ADDITIONAL RESEARCH FINDINGS:
{additional_research}

INSTRUCTIONS:
1. Review the initial outline and identify gaps or weak points
2. Incorporate relevant information from the additional research
3. Strengthen sections that lack depth or evidence
4. Ensure all key research findings are properly represented
5. Maintain the original structure unless significant improvements are needed

IMPROVED OUTLINE:"""
        )


# Create prompts instance for easy import
outline_prompts = OutlinePrompts()