import os
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

df = pd.read_excel("challenge.xlsx", index_col=None)
records = df.to_dict(orient="records")
print(records)
# Retrieve OpenAI API key
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

async def execute_task():
    for record in records:
        #print(record['First Name'])
        task_description = ("Go to https://rpachallenge.com/ then map corresponding values into form fields "
                            f"as follows: First Name as {record['First Name']}, Last Name as {record['Last Name']}, "
                            f"Company Name as {record['Company Name']}, Role in Company as {record['Role in Company']}, "
                            f"Address as {record['Address']}, Email as {record['Email']}, Phone Number as {record['Phone Number']}, "
                            "then click submit ")
        agent = Agent(
            task=task_description,
            llm=ChatOpenAI(model="gpt-4o"),
        )
        
        try:
            result = await agent.run()
            print(f"Task completed for {record['First Name']} {record['Last Name']}")
            print(result)
        except Exception as e:
            print(f"An error occurred for {record['First Name']} {record['Last Name']}: {e}")
        

def main():
    """Main function."""
    asyncio.run(execute_task())

if __name__ == "__main__":
    main()
