__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


import chromadb
client = chromadb.Client()
collection = client.get_collection(name="chroma_docs")
results = collection.get(ids=["page"])["documents"]
print(results) # Not found []


import streamlit as st
from research_matching.src.research_matching.crew import ResearchMatchingCrew  # Update to match your structure
import openai
import sys
import warnings

# try:
#     import pysqlite3
#     # Replace sqlite3 with pysqlite3
#     sys.modules['sqlite3'] = pysqlite3
# except ImportError:
#     warnings.warn(
#         "pysqlite3 not found. Using system sqlite3. "
#         "This might cause issues if your system sqlite3 version is < 3.35.0"
#     )
# except Exception as e:
#     warnings.warn(f"Error setting up pysqlite3: {str(e)}")


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
