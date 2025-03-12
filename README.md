Overview
This application matches company research interests with academic publications by analyzing a company's website and a publications directory. It uses AI to identify potential research collaborations and alignments between industry and academia.

Features
Analyzes company websites to extract research focus areas

Scans publication directories to find relevant academic research

Matches company interests with academic publications

Provides detailed reports on potential research collaborations

Installation
Prerequisites
Python 3.6+

Streamlit

OpenAI API key

Setup
Clone the repository

Install dependencies:

bash
pip install -r requirements.txt
Set up your OpenAI API key:

Add it to your environment variables: export OPENAI_API_KEY="your-api-key"

Or add it to Streamlit secrets

Usage
Run the Streamlit app:

bash
streamlit run app.py
Enter the company website URL you want to analyze

Enter the publications directory URL you want to match against

Click "Run Matching" to generate results

How It Works
The application uses the ResearchMatchingCrew class to:

Scrape and analyze the company website to identify research interests

Extract information from the publications directory

Use AI algorithms to find meaningful matches between company interests and academic research

Generate a comprehensive report of potential research collaborations

Configuration
The application uses Streamlit secrets or environment variables for configuration:

OPENAI_API_KEY: Your OpenAI API key for AI-powered analysis

Troubleshooting
If you encounter an error about missing API keys, ensure your OpenAI API key is properly set in environment variables or Streamlit secrets

For Docker deployment, uncomment the Python path configuration at the top of the file

Notes
The commented code at the top of the file is for Docker local deployment

The application requires internet access to analyze websites and publication directories
