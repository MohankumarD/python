"""Run `pip install yfinance` to install dependencies."""

from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

def get_compamy_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_compamy_symbol],
    show_tool_calls=True,
    instructions=["use tables to display data. "
                  "if you don't know the company symbol, please use get_company_symbol tool, even if it is not a piblic company"],
    markdown=True,
    debug_mode= True
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals from TSLA and Phidata")