from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found in environment variables. Please check your .env file."
    )

information = """
Elon Reeve Musk (/ˈiːlɒn mʌsk/; born June 28, 1971) is a businessman and U.S. special government employee, best known for his key roles in Tesla, Inc. and SpaceX, and his ownership of Twitter. Musk is the wealthiest individual in the world; as of February 2025, Forbes estimates his net worth to be US$397 billion. He has received several honors for his design and engineering work.

A member of the wealthy South African Musk family, Musk was born in Pretoria before immigrating to Canada, acquiring its citizenship. He moved to California in 1995 to attend Stanford University, and with his brother Kimbal co-founded the software company Zip2, that was later acquired by Compaq in 1999. That same year, Musk co-founded X.com, a direct bank, that later formed PayPal. In 2002, Musk acquired U.S. citizenship, and eBay acquired PayPal. Using the money he made from the sale, Musk founded SpaceX, a spaceflight services company, in 2002. In 2004, Musk was an early investor in electric vehicle manufacturer Tesla and became its chairman and later CEO. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk for fraud, alleging he falsely announced that he had secured funding for a private takeover of Tesla; he stepped down as chairman and paid a fine. In 2022, he acquired Twitter, and rebranded the service as X the following year.
"""

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

    chain = summary_prompt | llm

    res = chain.invoke(input={"information": information})

    print(res)
