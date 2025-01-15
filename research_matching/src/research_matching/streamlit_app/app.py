import streamlit as st
from research_matching.crew import ResearchMatchingCrew
import openai

# Just set the OpenAI API key directly
openai.api_key = st.secrets["OPENAI_API_KEY"]

def run_crew():
    st.title('Research Matching Mila App')
    
    company_website_url = st.text_input('Company Website URL', 'https://neclab.eu/')
    publications_directory = st.text_input('Publications Directory', 'https://mila.quebec/en/directory')
    
    if st.button('Run Crew'):
        crew = ResearchMatchingCrew()
        result = crew.crew().kickoff(inputs={
            "company_website_url": company_website_url,
            "publications_directory": publications_directory
        })
        st.write(result)

run_crew()

