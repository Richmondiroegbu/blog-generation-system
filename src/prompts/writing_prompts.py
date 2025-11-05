"""
Prompt templates for the Writing Agent.
Designed to guide the LLM in generating high-quality blog content.
"""

from langchain_core.prompts import PromptTemplate


class WritingPrompts:
    """Prompt templates for blog content generation."""
    
    @property
    def blog_generation_prompt(self) -> PromptTemplate:
        """
        Prompt for generating the full blog content from outline and research.
        """
        return PromptTemplate(
            input_variables=["topic", "outline", "research_summary", "current_date"],
            template="""You are a professional blog writer. Write a comprehensive, engaging blog post using the provided outline and research.

BLOG TOPIC: {topic}
CURRENT DATE: {current_date}

BLOG OUTLINE:
{outline}

RESEARCH SUMMARY:
{research_summary}

WRITING INSTRUCTIONS:
1. Follow the outline structure exactly
2. Use the research findings to support your content with facts and data
3. Write in an engaging, professional tone that educates readers
4. Include specific examples and practical insights
5. Ensure smooth transitions between sections
6. Aim for 1200-1500 words total

FORMATTING REQUIREMENTS:
- Use Markdown formatting
- Include headings and subheadings as in the outline
- Use bullet points for lists where appropriate
- **Bold** important concepts and key takeaways
- Write in clear, readable paragraphs

CONTENT QUALITY:
- Factual accuracy is paramount - only use information from the research
- Maintain logical flow throughout the article
- Balance depth with readability
- End with a strong conclusion that summarizes key insights

BLOG CONTENT (in Markdown):"""
        )
    
    @property
    def introduction_prompt(self) -> PromptTemplate:
        """
        Specialized prompt for writing compelling introductions.
        """
        return PromptTemplate(
            input_variables=["topic", "key_points", "target_audience"],
            template="""Write a compelling introduction for a blog post about '{topic}'.

TARGET AUDIENCE: {target_audience}

KEY POINTS THAT WILL BE COVERED:
{key_points}

INTRODUCTION REQUIREMENTS:
- Hook the reader in the first sentence
- Explain why this topic matters today
- Briefly mention what will be covered
- Set the appropriate tone for the blog
- Keep it concise (100-150 words)

INTRODUCTION:"""
        )
    
    @property
    def conclusion_prompt(self) -> PromptTemplate:
        """
        Specialized prompt for writing effective conclusions.
        """
        return PromptTemplate(
            input_variables=["topic", "main_insights", "future_implications"],
            template="""Write a powerful conclusion for a blog post about '{topic}'.

MAIN INSIGHTS COVERED:
{main_insights}

FUTURE IMPLICATIONS/TRENDS:
{future_implications}

CONCLUSION REQUIREMENTS:
- Summarize the key takeaways
- Reinforce the main message
- Suggest practical next steps or applications
- End with a memorable closing thought
- Keep it concise (100-150 words)

CONCLUSION:"""
        )


# Create prompts instance for easy import
writing_prompts = WritingPrompts()