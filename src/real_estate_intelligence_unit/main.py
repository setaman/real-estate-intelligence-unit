#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from real_estate_intelligence_unit.crew import RealEstateIntelligenceUnit

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        # 'portals': ", ".join(['https://www.kleinanzeigen.de/s-haus-kaufen/bungalow,einfamilienhaus,villa/nordrhein-westfalen/preis::500000/c208l928+haus_kaufen.haustyp_s:(bungalow%2Ceinfamilienhaus%2Cvilla)+options:haus_kaufen.celler_loft_b,haus_kaufen.garage_b']),
        'portals': ", ".join(['https://www.kleinanzeigen.de/s-haus-kaufen/bungalow,einfamilienhaus,villa/nordrhein-westfalen/preis::500000/c208l928+haus_kaufen.haustyp_s']),
        'current_year': str(datetime.now().year)
    }

    try:
        RealEstateIntelligenceUnit().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        RealEstateIntelligenceUnit().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        RealEstateIntelligenceUnit().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        RealEstateIntelligenceUnit().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
