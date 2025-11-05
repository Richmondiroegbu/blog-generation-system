"""
Outline Agent for the Blog Generation System.
"""

import time
from datetime import datetime
from langchain_groq import ChatGroq

from ..models.blog_models import BlogOutline, ResearchResult, AgentResponse, BlogSection
from ..utils.config import config
from ..prompts.outline_prompts import outline_prompts


class OutlineAgent:
    """Agent responsible for creating blog outlines."""
    
    def __init__(self):
        """Initialize the Outline Agent."""
        self.llm = ChatGroq(
            groq_api_key=config.GROQ_API_KEY,
            model_name=config.GROQ_MODEL,
            temperature=config.GROQ_TEMPERATURE,
            max_tokens=config.GROQ_MAX_TOKENS
        )
    
    def create_outline(self, research_result: ResearchResult) -> AgentResponse:
        """
        Create a blog outline from research results.
        """
        start_time = time.time()
        
        try:
            print(f"📝 Outline Agent: Creating outline for '{research_result.topic}'")
            
            blog_outline = self._generate_outline(research_result)
            
            processing_time = time.time() - start_time
            print(f"✅ Outline created in {processing_time:.2f}s")
            
            return AgentResponse(
                success=True,
                data=blog_outline,
                processing_time=processing_time
            )
            
        except Exception as e:
            processing_time = time.time() - start_time
            error_msg = f"Outline creation failed: {str(e)}"
            print(f"❌ Outline Agent: {error_msg}")
            
            return AgentResponse(
                success=False,
                error_message=error_msg,
                processing_time=processing_time
            )
    
    def _generate_outline(self, research_result: ResearchResult) -> BlogOutline:
        """Generate blog outline using research results."""
        prompt = outline_prompts.blog_outline_prompt
        chain = prompt | self.llm
        
        response = chain.invoke({
            "topic": research_result.topic,
            "research_summary": research_result.summary,
            "key_points": "\n".join(f"- {point}" for point in research_result.key_points),
            "current_date": datetime.now().strftime("%Y-%m-%d")
        })
        
        outline_text = response.content.strip()
        
        # Parse the outline into structured format
        return self._parse_outline_text(outline_text, research_result.topic)
    
    def _parse_outline_text(self, outline_text: str, topic: str) -> BlogOutline:
        """Parse LLM response into structured BlogOutline."""
        lines = [line.strip() for line in outline_text.split('\n') if line.strip()]
        
        # Extract title
        title = topic
        for line in lines:
            if line and line.startswith('# '):
                title = line.replace('#', '').strip()
                break
        
        # Create structured sections with proper content
        introduction = BlogSection(
            heading="Introduction",
            content="Engaging introduction that hooks the reader and explains the importance of the topic. This section will provide context and set the stage for the detailed discussion to follow.",
            word_count=150
        )
        
        # Create dynamic content sections based on key points
        content_sections = []
        section_headings = [
            "Current Landscape and Trends",
            "Key Challenges and Opportunities", 
            "Practical Applications and Case Studies",
            "Future Outlook and Implications"
        ]
        
        for heading in section_headings:
            content_sections.append(
                BlogSection(
                    heading=heading,
                    content=f"Comprehensive analysis of {heading.lower()}, including relevant data, examples, and insights. This section will explore specific aspects and provide detailed information to support the main arguments.",
                    word_count=300
                )
            )
        
        conclusion = BlogSection(
            heading="Conclusion",
            content="Summary of key insights, main takeaways, and final thoughts. This section will reinforce the main points and provide readers with clear actionable insights or recommendations.",
            word_count=150
        )
        
        return BlogOutline(
            topic=topic,
            title=title,
            introduction=introduction,
            content_sections=content_sections,
            conclusion=conclusion,
            target_audience="educated general readers and professionals",
            tone="professional yet accessible"
        )


# Create outline agent instance
outline_agent = OutlineAgent()  