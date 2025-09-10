import streamlit as st
from app.research_team import ResearchTeam

st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("Multi-Agent Research Assistant")

# Input: Research topic
topic = st.text_input("Enter your research topic:", "")

if st.button("Generate Research Report") and topic:
    with st.spinner("Generating research report... This may take a few minutes"):
        # Initialize ResearchTeam (coordinated multi-agent workflow)
        research_team = ResearchTeam(topic)
        report = research_team.print_response(topic)  # Collect output

    # Display the report
    st.subheader("Generated Research Report")
    st.markdown(report)
