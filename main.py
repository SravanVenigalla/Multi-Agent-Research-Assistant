"""
Main entry point for the Research Team application.
"""
from app.research_team import ResearchTeam

def main():
    """Main function to run research on a topic."""    
    # Define research topic
    topic = "What are the recent developments in NVIDIA GPUs"
    # Run research
    print(f"Starting research on: {topic}")
    research_team = ResearchTeam(topic)

    research_team.print_response(topic)

if __name__ == "__main__":
    main()