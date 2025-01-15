#!/usr/bin/env python
import sys
import warnings

from ..crew import ResearchMatchingCrew


# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'company_website_url': 'https://neclab.eu/',
        'publications_directory': 'https://mila.quebec/en/directory'
    }
    ResearchMatchingCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py run [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)