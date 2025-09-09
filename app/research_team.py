from agno.team.team import Team
from agno.models.groq import Groq
from app.agents.research_agent import Research_Agent
from app.agents.analysis_agent import Analysis_Agent
from app.agents.summary_agent import Summary_Agent
from app.knowledge import knowledge_base

def ResearchTeam(topic: str):
    knowledge = knowledge_base(topic)  # shared KBs for this topic

    return Team(
        name="ResearchTeam",
        mode="coordinate",
        model=Groq(id="gemma2-9b-it"),
        members=[Research_Agent, Analysis_Agent, Summary_Agent],
        description="You are the Senior Research Editor overseeing the workflow to ensure clarity, accuracy, and publication-ready outputs.",
        instructions=[
            "First, ask the ResearchAgent to collect references.",
            "Next, ask the AnalysisAgent to create a detailed report, using the shared knowledge base.",
            "Then, ask the SummariserAgent to condense the report into an executive summary.",
            "Review all outputs for editorial quality and consistency."
        ],
        knowledge=knowledge,
        add_datetime_to_instructions=True,
        enable_agentic_context=True,
        markdown=True,
        debug_mode=True,
        show_members_responses=True,
    )