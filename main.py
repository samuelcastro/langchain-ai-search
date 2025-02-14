from dotenv import load_dotenv

from typing import Tuple
# Prompt Templates: Prompt Templates in LangChain are a way to create reusable prompts for different chains.
from langchain_core.prompts import PromptTemplate

# Chain Models: Chain Models in LangChain are a way to chain together multiple components to form a larger chain.
from langchain_openai import ChatOpenAI

from output_parsers import Summary, summary_parser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.twitter import scrape_user_tweets


load_dotenv(override=True)

def search_agent(name: str) -> Tuple[Summary, str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_url, mock=True
    )

    twitter_url = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_url, mock=True)

    summary_template = """
        Given the information about a person from LinkedIn {information},
         and their latest twitter posts {twitter_posts} I want you to create:
        1. a short summary
        2. two interesting facts about them
        
        Use both the information from LinkedIn and the twitter posts.

        \n{format_instructions}
    """

    summary_prompt = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # Chain: A chain is a sequence of components that are executed in order.
    # Output Parsers: Output Parsers in LangChain are a way to parse the output of a chain.
    # chain = summary_prompt | llm | StrOutputParser()
    chain = summary_prompt | llm | summary_parser

    summary: Summary = chain.invoke(
        input={"information": linkedin_data, "twitter_posts": tweets}
    )

    res = summary, linkedin_data.get("photoUrl")

    return res


if __name__ == "__main__":
    print("AI Search Agent")

    search_agent(name="Harrison Chase")
