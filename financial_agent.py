from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

load_dotenv()

# OPENAI_API_KEY = os.getenv("OPEN_AI_API")


#web search agent
web_agent = Agent(

    name="Web Search Agent",
    role = "Search the web for the information",
    model=Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    markdown=True,
    show_tools_calls = True
)

finance_aget = Agent(

    name = "Finance AI Agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                           company_news=True)],
    instructions = ["Use table to display the data"],
    show_tool_calls = True,
    markdown = True

)

multi_ai_agent = Agent(

    team = [web_agent, finance_aget],
    model=Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    instructions=["Always include sources","Use table to display the data"],

    show_tool_calls = True,
    markdown = True

)

multi_ai_agent.print_response("Summarize Analyst recommendation and share latest news for NVDA", stream = True)