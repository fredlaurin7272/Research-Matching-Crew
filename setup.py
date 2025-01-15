from setuptools import setup, find_packages

setup(
    name="research_matching",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "openai",
        # Add other dependencies
    ],
)
