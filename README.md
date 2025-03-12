Overview
# Research Matching App

## Overview

This application matches company research interests with academic publications by analyzing a company's website and a publications directory. It uses AI to identify potential research collaborations and alignments between industry and academia.

## Features

- Analyzes company websites to extract research focus areas
- Scans publication directories to find relevant academic research
- Matches company interests with academic publications
- Provides detailed reports on potential research collaborations

## Installation

### Prerequisites

- Python 3.6+
- Streamlit
- OpenAI API key

### Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   - Add it to your environment variables: `export OPENAI_API_KEY="your-api-key"`
   - Or add it to Streamlit secrets

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Enter the company website URL you want to analyze
3. Enter the publications directory URL you want to match against
4. Click "Run Matching" to generate results

## How It Works

The application uses the `ResearchMatchingCrew` class to:
1. Scrape and analyze the company website to identify research interests
2. Extract information from the publications directory
3. Use AI algorithms to find meaningful matches between company interests and academic research
4. Generate a comprehensive report of potential research collaborations

## Configuration

The application uses Streamlit secrets or environment variables for configuration:
- `OPENAI_API_KEY`: Your OpenAI API key for AI-powered analysis

## Troubleshooting

- If you encounter an error about missing API keys, ensure your OpenAI API key is properly set in environment variables or Streamlit secrets
- For Docker deployment, uncomment the Python path configuration at the top of the file

## Notes

- The commented code at the top of the file is for Docker local deployment
- The application requires internet access to analyze websites and publication directories

---
Answer from Perplexity: pplx.ai/share
