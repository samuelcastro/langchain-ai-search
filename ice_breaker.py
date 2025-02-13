import os

# Output parsers
from langchain_core.output_parsers import StrOutputParser

# Prompt Templates: Prompt Templates in LangChain are a way to create reusable prompts for different chains.
from langchain_core.prompts import PromptTemplate

# Chain Models: Chain Models in LangChain are a way to chain together multiple components to form a larger chain.
from langchain_openai import ChatOpenAI

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

from dotenv import load_dotenv
from third_parties.twitter import scrape_user_tweets

load_dotenv(override=True)

# api_key = os.getenv("OPENAI_API_KEY")

# if not api_key:
#     raise ValueError(
#         "OPENAI_API_KEY not found in environment variables. Please check your .env file."
#     )


def ice_breaker_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)

    twitter_url = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_url, mock=True)

    summary_template = """
        Given the information about a person from LinkedIn {information},
         and twitter posts {twitter_posts} I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt = PromptTemplate(
        input_variables=["information", "twitter_posts"], template=summary_template
    )

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # Chain: A chain is a sequence of components that are executed in order.
    # Output Parsers: Output Parsers in LangChain are a way to parse the output of a chain.
    chain = summary_prompt | llm | StrOutputParser()

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/samuelcasilva/", mock=True
    )

    res = chain.invoke(input={"information": linkedin_data, "twitter_posts": tweets})

    print(res)


if __name__ == "__main__":
    print("Ice Breaker Enter")

    ice_breaker_with(name="Samuel Silva Evolua")
