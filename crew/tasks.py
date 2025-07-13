from crewai import Task

def create_tasks(product_idea_description):
    from crew.agents import (
        market_trend_analyst,
        competitor_intelligence_agent,
        target_audience_profiler,
        swot_specialist,
        product_strategy_consultant,
        report_generator
    )

    market_trend_task = Task(
                description=(
                    f"Analyze the current market trends, overall market size, and growth projections "
                    f"for the industry relevant to the product idea: '{product_idea_description}'. "
                    f"Identify key drivers, challenges, and general consumer behavior in this space."
                ),
                expected_output=(
                    "A detailed summary of relevant market trends, estimated market size, growth rate, "
                    "and influencing factors. Clearly state the target industry."
                ),
                agent=market_trend_analyst,
            )

            # Task 2: Competitor Analysis
    competitor_analysis_task = Task(
        description=(
            f"Identify and analyze primary and secondary competitors for the product idea: "
            f"'{product_idea_description}'. For each competitor, identify their main offerings, "
            f"pricing strategy (if discoverable), key strengths, and weaknesses. "
            f"Aim to find at least 3-5 competitors."
        ),
        expected_output=(
            "A list of key competitors with a brief analysis of their products, market positioning, "
            "strengths, and weaknesses relative to the described product idea."
        ),
        agent=competitor_intelligence_agent,
        context=[market_trend_task] # Provide market context to competitor agent
    )

    # Task 3: Target Audience Profiling
    target_audience_task = Task(
        description=(
            f"Based on the product idea: '{product_idea_description}' and identified market trends, "
            f"define the most likely target audience segments. Describe their demographics, "
            f"psychographics (values, attitudes, lifestyles), pain points this product addresses, "
            f"and how the product uniquely serves their needs."
        ),
        expected_output=(
            "A detailed profile of the primary and secondary target audience segments, "
            "including their characteristics, problems, and how the product provides solutions."
        ),
        agent=target_audience_profiler,
        context=[market_trend_task] # Use market context for audience definition
    )

    # Task 4: SWOT Analysis of the Product Idea
    swot_analysis_task = Task(
        description=(
            f"Perform a comprehensive SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis "
            f"specifically for the product idea: '{product_idea_description}'. "
            f"Strengths and Weaknesses are internal to the product/company. "
            f"Opportunities and Threats are external market factors. "
            f"Base this analysis on the insights from market trends, competitor analysis, and target audience profiling."
        ),
        expected_output=(
            "A structured SWOT analysis with clear points for Strengths, Weaknesses, "
            "Opportunities, and Threats relevant to the product idea."
        ),
        agent=swot_specialist,
        context=[market_trend_task, competitor_analysis_task, target_audience_task]
    )

    # Task 5: Strategic Recommendations
    strategic_recommendations_task = Task(
        description=(
            f"Synthesize all insights from the market trend analysis, competitor analysis, "
            f"target audience profiling, and SWOT analysis for the product idea: '{product_idea_description}'. "
            f"Provide actionable strategic recommendations addressing: "
            f"1. Market Entry Strategy (e.g., niche, pricing). "
            f"2. Key Differentiators/Unique Value Proposition. "
            f"3. Potential Challenges and Mitigation Strategies. "
            f"4. Next Steps for Product Development/Validation."
        ),
        expected_output=(
            "A concise section with strategic recommendations for the product idea, "
            "covering market entry, differentiation, risk mitigation, and future actions."
        ),
        agent=product_strategy_consultant,
        context=[market_trend_task, competitor_analysis_task, target_audience_task, swot_analysis_task]
    )

    # Task 6: Report Generation
    report_generation_task = Task(
        description=f"""
        Compile all the research findings and strategic recommendations into a professional, well-structured Market Research Report for the product idea: '{product_idea_description}'.

        The report MUST include the following sections in order:

        **1. Executive Summary:**
        - A brief overview of the product idea.
        - Key findings regarding market potential and viability.
        - A concluding statement on the overall outlook.

        **2. Product Idea Overview:**
        - Reiterate the product idea.
        - Briefly explain its core value proposition.

        **3. Market Analysis:**
        - Relevant Industry and Market Size.
        - Current Market Trends and Growth Drivers.
        - Key Market Challenges.

        **4. Competitor Landscape:**
        - Identification of Primary and Secondary Competitors.
        - Analysis of their offerings, pricing (if available), strengths, and weaknesses.
        - Differentiation opportunities for the product idea.

        **5. Target Audience Profile:**
        - Detailed description of primary and secondary customer segments.
        - Their demographics, psychographics, and relevant pain points.
        - How the product uniquely addresses their needs.

        **6. SWOT Analysis:**
        - Strengths of the product idea.
        - Weaknesses of the product idea.
        - Opportunities in the market for the product idea.
        - Threats from the market for the product idea.

        **7. Strategic Recommendations:**
        - Proposed Market Entry Strategy.
        - Recommended Unique Value Proposition.
        - Identified Potential Challenges and Mitigation Strategies.
        - Suggested Next Steps for Product Development/Validation.

        Ensure the report is clear, concise, and actionable. Use Markdown formatting for headings, bullet points, and emphasis.
        """,
        expected_output="A complete, well-formatted market research report in Markdown, following the specified structure.",
        agent=report_generator,
        context=[
            market_trend_task,
            competitor_analysis_task,
            target_audience_task,
            swot_analysis_task,
            strategic_recommendations_task
        ],
        output_file="market_research_report.md" # Saves the report to a file
    )

    return [
        market_trend_task,
        competitor_analysis_task,
        target_audience_task,
        swot_analysis_task,
        strategic_recommendations_task,
        report_generation_task
    ]