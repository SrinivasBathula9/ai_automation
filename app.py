import os
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()


# Retrieve OpenAI API key
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"] 

async def execute_task():
    """Executes the agent's task."""
    agent = Agent(
        #task="Go to https://www.youtube.com/@HarvestersTV, click on the first video and play it",
        task="Go to Yahoo finace web site , search for trending tickers then extract all of them into CSV files and save.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    try:
        result = await agent.run()       
        
        #print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        #result = await agent.run()
        df = pd.read_json(result)
        print("=====================",df)
        df.to_csv('output.csv')
        
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")    

def main():
    """Main function."""
    asyncio.run(execute_task())

if __name__ == "__main__":
    main()