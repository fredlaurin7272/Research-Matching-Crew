import streamlit as st
from src.research_matching.crew import ResearchMatchingCrew
import openai

# Just set the OpenAI API key directly
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Research Matching App")

company_website = st.text_input("Company Website URL", "https://neclab.eu/")
publications_dir = st.text_input("Publications Directory", "https://mila.quebec/en/directory")

if st.button("Run Matching"):
    inputs = {
        'company_website_url': company_website,
        'publications_directory': publications_dir
    }
    crew = ResearchMatchingCrew()
    results = crew.crew().kickoff(inputs=inputs)
    st.write(results)
