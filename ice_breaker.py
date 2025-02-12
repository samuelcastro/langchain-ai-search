# Output parsers
from langchain_core.output_parsers import StrOutputParser

# Prompt Templates: Prompt Templates in LangChain are a way to create reusable prompts for different chains.
from langchain_core.prompts import PromptTemplate

# Chain Models: Chain Models in LangChain are a way to chain together multiple components to form a larger chain.
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from third_parties.linkedin import scrape_linkedin_profile

from dotenv import load_dotenv
import os

load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found in environment variables. Please check your .env file."
    )

# This script prints a simple message when run directly.
# The special variable __name__ is set to "__main__" when the script is executed directly,
# as opposed to being imported into another module.
if __name__ == "__main__":
    print("Hello, LangChain test!")

    summary_template = """
    Given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
"""

    summary_prompt = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=api_key)
    # llm = ChatOllama(model="mistral", temperature=0)

    # Chain: A chain is a sequence of components that are executed in order.
    # Output Parsers: Output Parsers in LangChain are a way to parse the output of a chain.
    chain = summary_prompt | llm

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/samuelcasilva/"
    )

    res = chain.invoke(input={"information": linkedin_data})

    print(res)
