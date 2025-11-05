"""
Prompt templates for the Research Agent.
"""

from langchain_core.prompts import PromptTemplate


class ResearchPrompts:
    """Prompt templates for research operations."""
    
    @property
    def research_analysis_prompt(self) -> PromptTemplate:
        """
        Prompt for analyzing and synthesizing research materials.
        """
        return PromptTemplate(
            input_variables=["topic", "research_materials", "current_date"],
            template="""You are an expert research assistant. Analyze the research materials and create a comprehensive summary.

TOPIC: {topic}
DATE: {current_date}

RESEARCH MATERIALS:
{research_materials}

INSTRUCTIONS:
- Create a well-structured research summary (300-500 words)
- Focus on the most important and relevant information
- Extract key facts, data, and insights
- Organize information logically
- Maintain factual accuracy

RESEARCH SUMMARY:"""
        )
    
    @property
    def key_points_extraction_prompt(self) -> PromptTemplate:
        """
        Prompt for extracting key points from research summary.
        """
        return PromptTemplate(
            input_variables=["research_summary", "topic"],
            template="""Extract the key points from this research summary about '{topic}':

RESEARCH SUMMARY:
{research_summary}

INSTRUCTIONS:
- Extract 3-5 most important key points
- Each point should be a clear, concise statement
- Focus on unique insights and important facts
- Make each point standalone and meaningful

KEY POINTS (one per line, no bullets):"""
        )
    
    @property
    def research_queries_prompt(self) -> PromptTemplate:
        """
        Prompt for generating effective search queries.
        """
        return PromptTemplate(
            input_variables=["topic"],
            template="""Generate 3 specific search queries to research this topic: '{topic}'

INSTRUCTIONS:
- Make each query specific and researchable
- Cover different aspects of the topic
- Queries should be suitable for Wikipedia and web search
- Return only the queries, one per line

SEARCH QUERIES (one per line, no numbering):"""
        )


# Create prompts instance
research_prompts = ResearchPrompts()


















