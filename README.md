# 💡 Product Idea Validator & Market Researcher

> An AI-powered application leveraging CrewAI and Azure OpenAI to generate comprehensive market research reports for novel product ideas.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## 🚀 Demo Video

![Product Demo](assets\demo.gif)

## ✨ About the Project

In today's fast-paced market, validating new product ideas quickly and efficiently is crucial for entrepreneurs and innovators. Traditional market research can be time-consuming and expensive. This project introduces an autonomous AI agent crew designed to streamline this process.

This Streamlit application allows users to input a product idea, and then a crew of specialized AI agents collaboratively performs a preliminary market analysis, providing insights into market trends, competitors, target audiences, and a strategic SWOT analysis.

## 🌟 Features

* **Product Idea Input:** Easy-to-use Streamlit interface for describing your product.
* **Market Trend Analysis:** Identify industry growth, drivers, and challenges.
* **Competitor Intelligence:** Discover and analyze key rivals and their strategies.
* **Target Audience Profiling:** Define ideal customer segments and their needs.
* **SWOT Analysis:** Comprehensive assessment of product strengths, weaknesses, opportunities, and threats.
* **Strategic Recommendations:** Actionable advice for market entry and differentiation.
* **Comprehensive Report Generation:** Output a well-structured Markdown report for easy review.

## ⚙️ How It Works (Technical Overview)

This application is built on **CrewAI**, an orchestration framework for LLM-powered autonomous agents. It leverages **GPT-4o** model as the underlying large language model.

The core workflow involves a crew of six specialized AI agents working together:

1.  **Market Trend Analyst:** Researches and summarizes broad market conditions.
2.  **Competitor Intelligence Agent:** Scours for direct and indirect competitors, analyzing their offerings.
3.  **Target Audience Profiler:** Defines the potential customer base, their pain points, and needs.
4.  **SWOT Specialist:** Conducts a comprehensive SWOT analysis of the product idea, utilizing insights from previous agents.
5.  **Product Strategy Consultant:** Synthesizes all findings and generates actionable strategic recommendations.
6.  **Market Research Report Generator:** Compiles all the structured output into a cohesive, professional Markdown report.

The agents use a `web_search_tool` to gather information from the internet, simulating real-world research.

## 🚀 Setup and Installation

### Prerequisites

* Python 3.9+

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/kethan52/Multi-Agent-Product-Research.git](https://github.com/kethan52/Multi-Agent-Product-Research.git)
    cd your-project-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # On macOS/Linux:
    source .venv/bin/activate
    # On Windows (Command Prompt):
    .venv\Scripts\activate.bat
    # On Windows (PowerShell):
    .venv\Scripts\Activate.ps1
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Keys:**
    Create a `.env` file in the root of your project directory (`your-project-name/.env`) and add your credentials:
    ```
    
    ```
    **Important:** This `.env` file is excluded from version control by `.gitignore` for security.

## 🏃 Usage

1.  **Ensure your virtual environment is active.**
2.  **Run the Streamlit application:**
    ```bash
    streamlit run main.py
    ```
3.  Your browser will automatically open to the Streamlit app.
4.  Enter your product idea description in the text area and click "Generate Market Research Report".
5.  The AI agents will work in the background, and the comprehensive report will appear on the screen. You can also download it as a Markdown file.

## 📄 Example Report Output

You can find a sample generated report in the :
[market_research_report.md](market_research_report.md)

*(You'll create this file manually after generating a good report with your app)*

## 🤝 Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

* [CrewAI](https://www.crewai.com/)
* [Streamlit](https://streamlit.io/)
* [DuckDuckGo Search API](https://duckduckgo.com/api)
