import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# LangChain Tools are a way to add functionality to the agent.
from langchain_core.tools import Tool

# LangChain Agents are a way to create agents that can use tools to complete tasks.
# AgentExecutor is a way to execute agents.
# create_react_agent is a way to create a react agent which is a way to create a agent that can use tools to complete tasks.
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

# LangChain Hub is a way to existing prompts created by the community
from langchain import hub
from tools.tools import get_profile_url_tavily

load_dotenv(override=True)


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,  # 0 because we don't want any creative answers, we just need the results from the search
        model="gpt-4o-mini",
    )
    template = """
        Given the full name {name_of_person} I want you to find their LinkedIn profile URL. 
        Your final answer should only be a URL.
    """
    # Creating the prompt template to be used by the agent
    prompt = PromptTemplate(
        input_variables=["name_of_person"],
        template=template,
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile",  # name of the tool
            func=get_profile_url_tavily,  # This is the function that will be used by the agent
            description="useful when you need to get the LinkedIn URL of a person",  # description of the tool, this will help the agent to understand the tool
        )
    ]

    # Pulling the react prompt from the hub. The prompt is a way to guide the agent to use the tools correctly.
    react_prompt = hub.pull("hwchase17/react")

    # Creating the agent
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    # Creating the agent executor. This is a way to execute the agent.
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    # Executing the agent
    result = agent_executor.invoke({"input": prompt.format_prompt(name_of_person=name)})

    linkedin_profile_url = result["output"]

    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_profile_url = lookup(name="Samuel Silva")
    print(linkedin_profile_url)
