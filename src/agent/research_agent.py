#src/agents/research_agent.py

"""
Research Agent for the Blog Generation System.
"""

import time
from datetime import datetime
from typing import List
from langchain_groq import ChatGroq

from ..models.blog_models import ResearchResult, ResearchSource, AgentResponse
from ..utils.config import config
from ..tools.search_tools import search_tools
from ..prompts.research_prompts import research_prompts


class ResearchAgent:
    """Agent responsible for conducting research."""
    
    def __init__(self):
        """Initialize the Research Agent."""
        self.llm = ChatGroq(
            groq_api_key=config.GROQ_API_KEY,
            model_name=config.GROQ_MODEL,
            temperature=config.GROQ_TEMPERATURE,
            max_tokens=config.GROQ_MAX_TOKENS
        )
        
    def conduct_research(self, topic: str) -> AgentResponse:
        """
        Conduct comprehensive research.
        """
        start_time = time.time()
        
        try:
            print(f"🔍 Research Agent: Starting research on '{topic}'")
            
            # Generate search queries
            search_queries = self._generate_search_queries(topic)
            print(f"   Generated {len(search_queries)} search queries")
            
            # Perform research
            research_sources = self._perform_research(topic, search_queries)
            
            if not research_sources:
                return AgentResponse(
                    success=False,
                    error_message="No research materials found for the topic.",
                    processing_time=time.time() - start_time
                )
            
            # Analyze research
            research_summary, key_points = self._analyze_research(topic, research_sources)
            
            # Create ResearchResult
            research_result = ResearchResult(
                topic=topic,
                summary=research_summary,
                key_points=key_points,
                sources=research_sources,
                research_queries=search_queries
            )
            
            processing_time = time.time() - start_time
            print(f"✅ Research completed in {processing_time:.2f}s")
            
            return AgentResponse(
                success=True,
                data=research_result,
                processing_time=processing_time
            )
            
        except Exception as e:
            processing_time = time.time() - start_time
            error_msg = f"Research failed: {str(e)}"
            print(f"❌ Research Agent: {error_msg}")
            
            return AgentResponse(
                success=False,
                error_message=error_msg,
                processing_time=processing_time
            )
    
    def _generate_search_queries(self, topic: str) -> List[str]:
        """Generate search queries."""
        try:
            prompt = research_prompts.research_queries_prompt
            chain = prompt | self.llm
            
            response = chain.invoke({"topic": topic})
            queries_text = response.content.strip()
            
            # Parse queries properly
            queries = []
            for line in queries_text.split('\n'):
                line = line.strip()
                if line and len(line) > 10:  # Reasonable length check
                    # Remove numbering and bullets
                    clean_query = line.lstrip('1234567890.-•* ').strip()
                    if clean_query and not clean_query.startswith('Here are'):
                        queries.append(clean_query)
            
            return queries[:3] if queries else [topic]
            
        except Exception as e:
            print(f"⚠️ Query generation failed, using fallback: {e}")
            return [topic]
    
    def _perform_research(self, topic: str, queries: List[str]) -> List[ResearchSource]:
        """Perform research using search tools."""
        all_sources = []
        
        # Use only valid queries
        valid_queries = [q for q in queries if len(q) > 5 and len(q) < 100]
        research_queries = [topic] + valid_queries
        
        for query in research_queries[:2]:  # Limit to 2 queries
            print(f"   Researching: '{query}'")
            
            try:
                wiki_sources = search_tools.search_wikipedia(query)
                web_sources = search_tools.search_web(query)
                
                all_sources.extend(wiki_sources)
                all_sources.extend(web_sources)
            except Exception as e:
                print(f"⚠️ Research failed for '{query}': {e}")
                continue
        
        return all_sources[:4]  # Limit total sources
    
    def _analyze_research(self, topic: str, sources: List[ResearchSource]) -> tuple:
        """Analyze research materials."""
        try:
            # Prepare research materials
            research_materials = ""
            for i, source in enumerate(sources, 1):
                research_materials += f"Source {i} ({source.source_type}): {source.reference}\n"
                research_materials += f"Content: {source.content}\n\n"
            
            # Generate research summary
            prompt = research_prompts.research_analysis_prompt
            chain = prompt | self.llm
            
            response = chain.invoke({
                "topic": topic,
                "research_materials": research_materials,
                "current_date": datetime.now().strftime("%Y-%m-%d")
            })
            
            research_summary = response.content.strip()
            
            # Extract key points
            key_points = self._extract_key_points(research_summary, topic)
            
            return research_summary, key_points
            
        except Exception as e:
            print(f"⚠️ Research analysis failed: {e}")
            # Return fallback content
            fallback_summary = f"Research on {topic} revealed important insights about the subject. Key areas include current developments, challenges, and future prospects."
            fallback_points = [f"Important aspects of {topic}", f"Current trends in {topic}", f"Future implications of {topic}"]
            return fallback_summary, fallback_points
    
    def _extract_key_points(self, research_summary: str, topic: str) -> List[str]:
        """Extract key points from research summary."""
        try:
            prompt = research_prompts.key_points_extraction_prompt
            chain = prompt | self.llm
            
            response = chain.invoke({
                "research_summary": research_summary,
                "topic": topic
            })
            
            key_points_text = response.content.strip()
            key_points = []
            
            for line in key_points_text.split('\n'):
                line = line.strip()
                if line and len(line) > 10:
                    # Clean the line
                    clean_point = line.lstrip('1234567890.-•* ').strip()
                    if clean_point and not clean_point.startswith('KEY POINTS'):
                        key_points.append(clean_point)
            
            return key_points[:5] if key_points else [f"Key information about {topic}"]
            
        except Exception as e:
            print(f"⚠️ Key points extraction failed: {e}")
            return [f"Important aspects of {topic}"]


# Create research agent instance
research_agent = ResearchAgent()











