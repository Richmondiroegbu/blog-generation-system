"""
Main orchestration script for the Blog Generation System.
"""

import time
import sys
import os
from datetime import datetime
from typing import Optional

# Fix import paths - use relative imports
from src.utils.config import config
from src.models.blog_models import GeneratedBlog
from src.agents.research_agent import research_agent
from src.agents.outline_agent import outline_agent
from src.agents.writing_agent import writing_agent
from src.utils.file_handlers import file_handlers


class BlogGenerationSystem:
    """Main orchestrator for the blog generation pipeline."""
    
    def __init__(self):
        """Initialize the system."""
        self.system_start_time = None
        self.total_processing_time = None
        
    def generate_blog(self, topic: str, save_to_file: bool = True) -> Optional[GeneratedBlog]:
        """Generate a complete blog post."""
        self.system_start_time = time.time()
        
        print("=" * 60)
        print("🚀 BLOG GENERATION SYSTEM - Starting Pipeline")
        print("=" * 60)
        print(f"Topic: {topic}")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        try:
            # Validate configuration
            config.validate_config()
            print("✅ Configuration validated")
            
            # Step 1: Research Phase
            print("\n" + "=" * 40)
            print("PHASE 1: RESEARCH")
            print("=" * 40)
            
            research_response = research_agent.conduct_research(topic)
            if not research_response.success:
                print(f"❌ Research failed: {research_response.error_message}")
                return None
                
            research_result = research_response.data
            print(f"✅ Research completed: {len(research_result.sources)} sources")
            
            # Step 2: Outline Phase
            print("\n" + "=" * 40)
            print("PHASE 2: OUTLINING") 
            print("=" * 40)
            
            outline_response = outline_agent.create_outline(research_result)
            if not outline_response.success:
                print(f"❌ Outline failed: {outline_response.error_message}")
                return None
                
            blog_outline = outline_response.data
            print(f"✅ Outline created: '{blog_outline.title}'")
            
            # Step 3: Writing Phase
            print("\n" + "=" * 40)
            print("PHASE 3: WRITING")
            print("=" * 40)
            
            writing_response = writing_agent.write_blog(blog_outline, research_result)
            if not writing_response.success:
                print(f"❌ Writing failed: {writing_response.error_message}")
                return None
                
            generated_blog = writing_response.data
            self.total_processing_time = time.time() - self.system_start_time
            
            # Display results
            self._display_results(generated_blog)
            
            # Save to file
            if save_to_file:
                filepath = file_handlers.save_blog_to_file(generated_blog)
                file_handlers.save_metadata(generated_blog, filepath)
                print(f"✅ Output saved to: {filepath}")
            
            return generated_blog
            
        except Exception as e:
            self.total_processing_time = time.time() - self.system_start_time
            print(f"❌ System error: {str(e)}")
            import traceback
            traceback.print_exc()
            return None
    
    def _display_results(self, blog: GeneratedBlog):
        """Display generation results."""
        print("\n" + "=" * 50)
        print("🎉 BLOG GENERATION COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        print(f"⏱️  Total processing time: {self.total_processing_time:.2f}s")
        print(f"📊 Word count: {blog.word_count} words")
        print(f"📚 Sources used: {len(blog.research_sources)}")
        print()
        
        # Display formatted blog content
        print("📄 GENERATED BLOG CONTENT:")
        print("=" * 60)
        print(blog.content)
        print("=" * 60)
    
    def run_from_cli(self):
        """Run from command line."""
        if len(sys.argv) < 2:
            print("Usage: python run.py \"Your blog topic here\"")
            print("Example: python run.py \"The Future of Artificial Intelligence\"")
            sys.exit(1)
        
        topic = " ".join(sys.argv[1:])
        result = self.generate_blog(topic)
        
        if not result:
            print("❌ Blog generation failed.")
            sys.exit(1)


def main():
    """Main entry point."""
    system = BlogGenerationSystem()
    
    if len(sys.argv) > 1:
        system.run_from_cli()
    else:
        # Interactive mode
        print("🤖 Welcome to the Blog Generation System!")
        print()
        
        while True:
            topic = input("Enter a blog topic (or 'quit' to exit): ").strip()
            
            if topic.lower() in ['quit', 'exit', 'q']:
                print("👋 Thank you for using the system!")
                break
                
            if not topic:
                print("❌ Please enter a valid topic.")
                continue
                
            print()
            result = system.generate_blog(topic)
            
            if not result:
                print("❌ Generation failed. Please try again.")
            
            print("\n" + "=" * 60)
            print()


if __name__ == "__main__":
    main()



