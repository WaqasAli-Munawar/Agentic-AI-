from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
import phi
from phi.playground import Playground, serve_playground_app

load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

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

app = Playground(agents=[web_agent,finance_aget]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app", reload = True)



