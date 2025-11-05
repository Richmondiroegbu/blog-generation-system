
#src/agents/writing_agent.py

"""
Writing Agent for the Blog Generation System.
"""

import time
from datetime import datetime
from langchain_groq import ChatGroq

from ..models.blog_models import GeneratedBlog, BlogOutline, ResearchResult, AgentResponse
from ..utils.config import config
from ..prompts.writing_prompts import writing_prompts


class WritingAgent:
    """Agent responsible for generating blog content."""
    
    def __init__(self):
        """Initialize the Writing Agent."""
        self.llm = ChatGroq(
            groq_api_key=config.GROQ_API_KEY,
            model_name=config.GROQ_MODEL,
            temperature=config.GROQ_TEMPERATURE,
            max_tokens=config.GROQ_MAX_TOKENS
        )
    
    def write_blog(self, outline: BlogOutline, research_result: ResearchResult) -> AgentResponse:
        """
        Write complete blog content.
        """
        start_time = time.time()
        
        try:
            print(f"✍️ Writing Agent: Writing blog '{outline.title}'")
            
            blog_content = self._generate_blog_content(outline, research_result)
            word_count = self._count_words(blog_content)
            
            generated_blog = GeneratedBlog(
                outline=outline,
                content=blog_content,
                word_count=word_count,
                research_sources=research_result.sources,
                generation_metadata={
                    "research_queries_used": research_result.research_queries,
                    "key_points_covered": research_result.key_points,
                    "generation_timestamp": datetime.now().isoformat()
                }
            )
            
            processing_time = time.time() - start_time
            print(f"✅ Writing completed in {processing_time:.2f}s")
            print(f"   Word count: {word_count}")
            
            return AgentResponse(
                success=True,
                data=generated_blog,
                processing_time=processing_time
            )
            
        except Exception as e:
            processing_time = time.time() - start_time
            error_msg = f"Blog writing failed: {str(e)}"
            print(f"❌ Writing Agent: {error_msg}")
            
            return AgentResponse(
                success=False,
                error_message=error_msg,
                processing_time=processing_time
            )
    
    def _generate_blog_content(self, outline: BlogOutline, research_result: ResearchResult) -> str:
        """Generate blog content using outline and research."""
        outline_str = self._format_outline_for_prompt(outline)
        
        prompt = writing_prompts.blog_generation_prompt
        chain = prompt | self.llm
        
        response = chain.invoke({
            "topic": outline.topic,
            "outline": outline_str,
            "research_summary": research_result.summary,
            "current_date": datetime.now().strftime("%Y-%m-%d")
        })
        
        return self._format_blog_content(response.content.strip())
    
    def _format_outline_for_prompt(self, outline: BlogOutline) -> str:
        """Format BlogOutline for the prompt."""
        outline_lines = []
        outline_lines.append(f"# {outline.title}")
        outline_lines.append("")
        outline_lines.append("## Introduction")
        outline_lines.append(f"{outline.introduction.content}")
        outline_lines.append("")
        
        outline_lines.append("## Content")
        for section in outline.content_sections:
            outline_lines.append(f"### {section.heading}")
            outline_lines.append(f"{section.content}")
            outline_lines.append("")
        
        outline_lines.append("## Summary")
        outline_lines.append(f"{outline.conclusion.content}")
        outline_lines.append("")
        outline_lines.append(f"**Target Audience**: {outline.target_audience}")
        outline_lines.append(f"**Tone**: {outline.tone}")
        
        return "\n".join(outline_lines)
    
    def _format_blog_content(self, content: str) -> str:
        """Ensure proper formatting of blog content."""
        lines = content.split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if line.startswith('## '):
                # Ensure proper heading format
                formatted_lines.append(f"## {line[3:].strip()}")
            elif line.startswith('### '):
                formatted_lines.append(f"### {line[4:].strip()}")
            else:
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    def _count_words(self, text: str) -> int:
        """Count words in text."""
        return len(text.split())


# Create writing agent instance
writing_agent = WritingAgent()