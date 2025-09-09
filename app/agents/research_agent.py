from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from agno.tools.arxiv import ArxivTools
from app.config import GROQ_API_KEY

Research_Agent = Agent(
    name="ResearchAgent",
    model=Groq(id="gemma2-9b-it"),
    description=(
        "You are a Research Journalist. "
        "Your role is to investigate a topic thoroughly by collecting diverse, high-quality references. "
        "You specialize in finding reliable sources across blogs, articles, encyclopedic entries, and academic research papers."
    ),
    instructions=[
        "Search the web, Wikipedia, and academic sources for the given topic.",
        "Curate 15â€“25 of the most relevant sources, ensuring a balanced mix of blogs, encyclopedic entries, and research papers.",
        "Organize results into three sections: **Articles & Blogs**, **Encyclopedic Knowledge**, and **Research Papers**.",
        "For each source, provide: direct link, title (if available), and a 1â€“2 sentence summary.",
        "Return results in clean Markdown format with bullet points."
    ],
    tools=[DuckDuckGoTools(), WikipediaTools(), ArxivTools()],
    show_tool_calls=True,
    markdown=True
)