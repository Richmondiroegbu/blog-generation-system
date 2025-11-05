# blog-generation-system
Blog generation multi-agent system




Blog Generation System
A sophisticated agent-based system for generating well-researched blog posts using AI agents. This system automates the entire blog creation process from research to final content generation.


Features
 - Multi-Agent Architecture: Specialized agents for research, outlining, and writing

 - Intelligent Research: Automated research using Wikipedia and web search

 - Structured Content: Well-organized blog outlines with logical flow

 - Professional Writing: High-quality content generation with proper formatting

 - Configurable: Easy-to-modify prompts and settings

 - Markdown Output: Clean, formatted blog posts ready for publishing


Project Structure


blog-generation-system/
├── src/
│   ├── agents/              # Specialized AI agents
│   │   ├── research_agent.py
│   │   ├── outline_agent.py
│   │   └── writing_agent.py
│   ├── models/              # Data models
│   │   └── blog_models.py
│   ├── prompts/             # LLM prompt templates
│   │   ├── research_prompts.py
│   │   ├── outline_prompts.py
│   │   └── writing_prompts.py
│   ├── tools/               # Utility tools
│   │   ├── search_tools.py
│   │   └── text_utils.py
│   ├── utils/               # Configuration and utilities
│   │   ├── config.py
│   │   └── file_handlers.py
│   └── main.py              # Main orchestration script
├── examples/                # Sample inputs and outputs
│   ├── input/
│   └── output/
├── requirements.txt         # Python dependencies
└── README.md               # This file

🛠 Installation 

Prerequisites
Python 3.8 or higher

Groq API key



Step-by-Step Setup

1. Clone the Repository

bash
git clone https://github.com/Richmondiroegbu/blog-generation-system.git
cd blog-generation-system


2. Create Virtual Environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install Dependencies

bash
pip install -r requirements.txt


4. Environment Configuration

bash
# Create .env file
create a .env file

env
GROQ_API_KEY=your_actual_groq_api_key


Usage

Command Line Interface

1. Interactive Mode

bash
python -m src.main
Then enter your blog topic when prompted.

2. Direct Topic Input

bash
python -m src.main "The Future of Artificial Intelligence in Healthcare"


3. Using Python Script

python
from src.main import BlogGenerationSystem

system = BlogGenerationSystem()
blog = system.generate_blog("Your blog topic here")


Example Usage

python
# Basic usage
from src.main import BlogGenerationSystem

system = BlogGenerationSystem()
result = system.generate_blog("Sustainable Energy Solutions")

if result:
    print(f"Blog generated successfully! Word count: {result.word_count}")



Sample Inputs and Outputs

Sample Input Topics

 - "The Impact of AI on Modern Education"

 - "Blockchain Technology in Supply Chain Management"

 - "Renewable Energy Trends in 2024"

 - "Mental Health in the Digital Age"

Sample Output Structure
text
Generated Blog: "The Future of AI in Healthcare"
├── Introduction (150 words)
├── Current Landscape and Trends (300 words)
├── Key Challenges and Opportunities (300 words)
├── Practical Applications (300 words)
├── Future Outlook (300 words)
└── Conclusion (150 words)
Total: ~1500 words


Configuration
Key Configuration Options
Edit src/utils/config.py to modify:

python
# Model Settings
GROQ_MODEL = "llama-3.1-8b-instant"  # Alternative: "mixtral-8x7b-32768"
GROQ_TEMPERATURE = 0.3              # Creativity level (0.0-1.0)
GROQ_MAX_TOKENS = 4000              # Maximum response length

# Content Settings
MAX_BLOG_LENGTH = 1500              # Target word count
MAX_RESEARCH_WORDS = 800            # Research content limit


Development

Adding New Agents

1. Create agent in src/agents/

2. Add to src/agents/__init__.py

3. Create prompts in src/prompts/

4. Update main orchestration


Customizing Prompts

Modify prompt templates in:

 - src/prompts/research_prompts.py

 - src/prompts/outline_prompts.py

 - src/prompts/writing_prompts.py


Troubleshooting
Common Issues
1. API Key Error

text
Error: GROQ_API_KEY not found
Solution: Ensure .env file exists with correct API key

2. Module Import Errors

text
ModuleNotFoundError: No module named 'src'
Solution: Run from project root directory or adjust Python path

3. Network Timeouts

text
Request timeout during research
Solution: Check internet connection, retry with simpler topic

Debug Mode
Enable detailed logging by modifying src/utils/config.py:

python
DEBUG = True


Performance
Typical Processing Times

 - Research Phase: 10-20 seconds

 - utline Generation: 5-10 seconds

 - Content Writing: 15-30 seconds

 - Total: 30-60 seconds per blog

Quality Metrics
 - Word Count: 1200-1500 words

 - Source Integration: 3-5 research sources

 - Structure: 5-7 well-organized sections


Future Improvements

Planned Enhancements

1. Enhanced Research

 - Integration with academic databases

 - Real-time news API integration

 - Source credibility scoring

2. Content Quality

 - Fact-checking mechanisms

 - Plagiarism detection

 - SEO optimization

3. User Experience

 - Web interface

 - Content customization options

 - Multiple output formats

3. Advanced Features

 - Multi-language support


Known Limitation

1. Research Depth

 - Currently uses simplified search tools

 - Limited to publicly available sources

2. Content Originality

 - Relies on LLM generation without human review

 - May require fact verification for sensitive topics

3. Customization

 - Limited tone/style customization options

 - Fixed blog structure template

Contributing
1. Fork the repository

2. Create a feature branch

3. Make your changes

4. Add tests if applicable

5. Submit a pull request


License
This project is for educational and demonstration purposes as part of an internship assignment.

Support
For issues and questions:

1. Check the troubleshooting section

2. Review sample configurations

3. Ensure all dependencies are installed

4. Verify API key validity

