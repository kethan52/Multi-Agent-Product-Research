from crewai import Crew
from crew.tasks import create_tasks
from crew.agents import *

def setup_crew(product_idea_description):
    tasks = create_tasks(product_idea_description)
    crew = Crew(
        agents=[
            market_trend_analyst,
            competitor_intelligence_agent,
            target_audience_profiler,
            swot_specialist,
            product_strategy_consultant,
            report_generator
        ],
        tasks=tasks,
        verbose=True
    )
    return crew
