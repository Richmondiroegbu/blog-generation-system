"""
File handling utilities for the Blog Generation System.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

# Fix relative imports
try:
    from models.blog_models import GeneratedBlog
except ImportError:
    # Fallback for direct execution
    from ..models.blog_models import GeneratedBlog


class FileHandlers:
    """Utility class for file operations."""
    
    @staticmethod
    def ensure_directory(path: str) -> Path:
        """
        Ensure a directory exists, create if it doesn't.
        
        Args:
            path: Directory path
            
        Returns:
            Path object for the directory
        """
        path_obj = Path(path)
        path_obj.mkdir(parents=True, exist_ok=True)
        return path_obj
    
    @staticmethod
    def save_blog_to_file(blog: GeneratedBlog, filename: str = None) -> str:
        """
        Save generated blog to a markdown file.
        
        Args:
            blog: GeneratedBlog object to save
            filename: Optional custom filename
            
        Returns:
            Path to the saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_topic = "".join(c for c in blog.outline.topic if c.isalnum() or c in (' ', '-', '_')).rstrip()
            safe_topic = safe_topic.replace(' ', '_')[:50]
            filename = f"blog_{safe_topic}_{timestamp}.md"
        
        output_dir = FileHandlers.ensure_directory("examples/output")
        filepath = output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(blog.content)
        
        print(f"✅ Blog saved to: {filepath}")
        return str(filepath)
    
    @staticmethod
    def save_metadata(blog: GeneratedBlog, filepath: str) -> str:
        """
        Save generation metadata to a JSON file.
        
        Args:
            blog: GeneratedBlog object
            filepath: Path to the corresponding blog file
            
        Returns:
            Path to the metadata file
        """
        metadata = {
            "topic": blog.outline.topic,
            "title": blog.outline.title,
            "word_count": blog.word_count,
            "generation_timestamp": datetime.now().isoformat(),
            "sources_used": len(blog.research_sources),
            "generation_metadata": blog.generation_metadata
        }
        
        metadata_path = Path(filepath).with_suffix('.json')
        
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        return str(metadata_path)


# Create file handler instance for easy import
file_handlers = FileHandlers()
















